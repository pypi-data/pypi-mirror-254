import pandas as pd
from geopy.distance import geodesic
from datetime import datetime, timedelta
import plotly.express as px
import os

def calculate_distance(lat, lon, df_deviceid_file_path, distance, row_lat='lat', row_lon='lon', deviceid='device_id'):
    # Read the device data from the CSV file
    df_deviceid = pd.read_csv(df_deviceid_file_path)
    
    # Drop rows with missing lat or lon values
    df_deviceid = df_deviceid.dropna(subset=[row_lat, row_lon], how='all')
    
    # Ensure latitude and longitude values are within valid ranges
    min_lat = -90
    max_lat = 90
    min_lon = -180
    max_lon = 180
    df_deviceid[row_lat] = df_deviceid[row_lat].apply(lambda x: min(max(min_lat, x), max_lat))
    df_deviceid[row_lon] = df_deviceid[row_lon].apply(lambda x: min(max(min_lon, x), max_lon))

    # Create a function to calculate the distance
    def calculate_distance_row(row):
        device_location = (row[row_lat], row[row_lon])
        target_location = (lat, lon)
        distance = geodesic(device_location, target_location).kilometers
        return distance

    # Add a column to store the distances
    df_deviceid['distance_km'] = df_deviceid.apply(calculate_distance_row, axis=1)

    # Filter out data within one kilometer
    filtered_df = df_deviceid[df_deviceid['distance_km'] <= distance]

    # Get the list of device IDs
    lst_device_id = filtered_df[deviceid].to_list()

    return lst_device_id

def filter_data_for_device(result_lst_device_id, time, df_device_file_path, row_time='localTime', row_deviceid='deviceId', sensor='pm2_5', ten_minutes_before_after=4):
    def get_date_hour_min(time_diff, base_time):
        # 計算新時間
        new_time = base_time + timedelta(minutes=time_diff)

        # 格式化日期和時間
        str_date = new_time.strftime("%Y-%m-%d")
        str_hour = new_time.strftime("%H")
        str_minute = new_time.strftime("%M")[0]

        return str_date, str_hour, str_minute

    def filter_time(df, time):
        user_input_time = pd.to_datetime(time)
        half_hour_offset = pd.DateOffset(minutes=30)
        start_time = user_input_time - half_hour_offset
        end_time = user_input_time + half_hour_offset
        df[row_time] = pd.to_datetime(df[row_time])
        filtered_data = df[(df[row_time] >= start_time) & (df[row_time] <= end_time)].reset_index(drop=True)
        return filtered_data

    def filter_deviceid(df, result_lst_device_id):
        df = df[df[row_deviceid].isin(result_lst_device_id)].reset_index(drop=True)
        return df

    df_all = pd.DataFrame()
    base_time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')

    for i in range(-10 * ten_minutes_before_after, 10 * ten_minutes_before_after, 10):
        str_date, str_hour, str_minute = get_date_hour_min(i, base_time)
        str_url = f'{df_device_file_path}/{str_date}/10mins_{str_date}_{str_hour}_{str_minute}.csv.gz'
        try:
            df = pd.read_csv(str_url, compression='gzip')
            df_all = pd.concat([df_all, df], ignore_index=True)
        except:
            pass
    df_all = filter_time(df_all, time)
    df_all = filter_deviceid(df_all, result_lst_device_id)
    df_all = df_all[df_all['sensorId'] == sensor].reset_index(drop=True)
    return df_all
    

def create_custom_color_scale(color_dict):
    scale = []
    max_value = max(item['v'] for item in color_dict)  # 獲取最大數值
    for item in color_dict:
        # 將每個色彩值對應到其數值範圍（從0到1之間），並反轉色彩順序
        scale.append([item['v'] / max_value, item['color']])
    return scale[::-1]  # 反轉色彩尺度列表

def create_pm25_map(df, lat, lon, file_path, row_value='value', row_deviceId='deviceId', row_lat='lat', row_lon='lon',
                    row_time='localTime'):
    # Filter data
    df[row_value] = df[row_value].astype(float)
    df = df.loc[df.groupby(row_deviceId)[row_value].idxmax()]

    pm2_5_color_dict = [
        {"v": 500.4, "color": "#000000"},
        {"v": 450.5, "color": "#301E12"},
        {"v": 400.5, "color": "#3C230F"},
        {"v": 350.5, "color": "#49280D"},
        {"v": 300.5, "color": "#552E0A"},
        {"v": 250.5, "color": "#623307"},
        {"v": 230.5, "color": "#682c1f"},
        {"v": 210.5, "color": "#6d2537"},
        {"v": 190.5, "color": "#731d4e"},
        {"v": 170.5, "color": "#781666"},
        {"v": 150.5, "color": "#7e0f7e"},
        {"v": 131.3, "color": "#970f6a"},
        {"v": 112.1, "color": "#b10f56"},
        {"v": 92.9, "color": "#ca0e43"},
        {"v": 73.7, "color": "#e30e30"},
        {"v": 54.5, "color": "#fc0e1c"},
        {"v": 50.7, "color": "#fc241d"},
        {"v": 46.9, "color": "#fc3b1f"},
        {"v": 43.1, "color": "#fd5220"},
        {"v": 39.3, "color": "#fd6822"},
        {"v": 35.5, "color": "#fd7e23"},
        {"v": 31.5, "color": "#fd9827"},
        {"v": 27.5, "color": "#feb12b"},
        {"v": 23.5, "color": "#fecb30"},
        {"v": 19.5, "color": "#ffe534"},
        {"v": 15.5, "color": "#fffd38"},
        {"v": 12.4, "color": "#d4fd36"},
        {"v": 9.3, "color": "#a9fd34"},
        {"v": 6.2, "color": "#7EFD32"},
        {"v": 3.1, "color": "#53FD30"},
        {"v": 0, "color": "#29fd2e"}
    ]
    custom_color_scale = create_custom_color_scale(pm2_5_color_dict)

    # Create scatter mapbox
    fig = px.scatter_mapbox(df, lat=row_lat, lon=row_lon, color=row_value, range_color=(0, 500.4),
                            hover_data=[row_time, row_deviceId, row_value], zoom=7, size=[15] * len(df[row_lat]),
                            size_max=15, color_continuous_scale=custom_color_scale)

    fig.update_layout(mapbox_style='open-street-map')  # carto-positron

    initial_center = {"lat": lat, "lon": lon}  # Example coordinates
    initial_zoom = 14  # Example zoom level
    fig.update_layout(mapbox_center=initial_center, mapbox_zoom=initial_zoom)

    fig.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})


    # Save to html
    fig.write_html(file_path, include_plotlyjs=True)

    return file_path


if __name__ == '__main__':
    # Example of calculate_distance usage:
    lon = 121.4471
    lat = 25.0669
    df_deviceid_file_path = '/Users/apple/Downloads/project_device_table_20231017.csv'
    result_lst_device_id = calculate_distance(lat, lon, df_deviceid_file_path, 1)
    print(result_lst_device_id)
    
    # Example of filter_data_for_device_time usage:
    df_device_file_path = '/Users/apple/Desktop/iot_data'
    time = '2023-11-03 08:35:00'
    df = filter_data_for_device(result_lst_device_id, time,df_device_file_path)
    print(df.localTime.min())
    print(df.localTime.max())
    print(df.columns)
    
    file_path = '/Users/apple/Desktop/test.html'
    url = create_pm25_map(df,lat, lon, file_path, row_value='value', row_deviceId='deviceId', row_lat='lat', row_lon='lon', row_time='localTime')
    print(url)
