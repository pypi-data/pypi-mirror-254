from geopandas import GeoDataFrame
from geopandas import points_from_xy
from shapely.geometry import mapping, Point, Polygon
from sklearn.cluster import DBSCAN

########################### Polygon Map ###########################
class polygon_map:
    def __init__(self):
        pass
    

    def Left_index(self, points):
        minn = 0
        for i in range(1,len(points)):
            if points[i].x < points[minn].x:
                minn = i
            elif points[i].x == points[minn].x:
                if points[i].y > points[minn].y:
                    minn = i
        return minn

    
    def orientation(self, p, q, r):
        val = (q.y - p.y) * (r.x - q.x) - \
            (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

        
    def convexHull(self, points, n):
        if n < 3:
            return
        l = self.Left_index(points)
        hull = []
        p = l
        q = 0
        while(True):
            hull.append(p)
            q = (p + 1) % n
            for i in range(n):
                if(self.orientation(points[p],
                            points[i], points[q]) == 2):
                    q = i
            p = q
            if(p == l):
                break
        lon = []
        lat = []
        for each in hull:
            lon.append(points[each].x)
            lat.append(points[each].y)
        return lon, lat

    
    def cluster_creator(self, df, index_list, eps, min_samples, metric, metric_params, algorithm, leaf_size, p, n_jobs):
        model = DBSCAN(eps=eps, min_samples=min_samples, metric=metric, metric_params=metric_params, algorithm=algorithm, leaf_size=leaf_size, p=p, n_jobs=n_jobs)
        prediction = model.fit_predict(df[index_list])
        pred = pd.DataFrame(prediction, columns=['cluster_group'])
        df = df.join(pred)
        return df

    
    def polygon_creator(self, df, longitude, latitude):
        lon = df[longitude]
        lat = df[latitude]
        df = GeoDataFrame(df, geometry=points_from_xy(lon, lat))
        df.rename(columns={"geometry": "points"}, inplace=True)
        points = [Point(x,y) for x,y in zip(lon, lat)]
        new_lon, new_lat = self.convexHull(points, len(points))
        polygon_geom = [Polygon(zip(new_lon, new_lat))]*len(df)
        crs = 'epsg:4326'
        df = GeoDataFrame(df, crs=crs, geometry=polygon_geom)  
        return df

    
    def map_creator(self, df, index_list, eps=0.5, min_samples=5, metric='euclidean', metric_params=None, algorithm='auto', leaf_size=30, p=None, n_jobs=None):
        df = self.cluster_creator(df, index_list, eps=eps, min_samples=min_samples, metric=metric, metric_params=metric_params, algorithm=algorithm, leaf_size=leaf_size, p=p, n_jobs=n_jobs)
        n_clusters = len(set(df['cluster_group']))
        df_list = []
        for cluster in range(n_clusters):
            part_df = df[df['cluster_group']==cluster]
            part_df = self.polygon_creator(part_df, 'Long', 'Lat')
            df_list.append(part_df)
        total_df = pd.concat(df_list, ignore_index=False)
        return total_df

    
    def boundary_test(self, acct_name, polygon, points):
        if polygon.contains(points):
            print("{} is in the polygon...".format(acct_name))
        elif polygon.touches(points):
            print("{} is in the polygon...".format(acct_name))
        else:
            print("Not in the polygon...")




