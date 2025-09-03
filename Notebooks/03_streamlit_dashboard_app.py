import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import datetime

@st.cache_data
def load_data():
  data = pd.read_csv("../dataset/processed_dataset.csv")
  return data

df = load_data() 

st.set_page_config(
  page_title = "Bengaluru Traffic Analysis",
  layout = "wide"
)

st.title("🚦Bengaluru Traffic Analysis Dashboard")
st.markdown("A deep dive into traffic patterns, congestion, and average speeds to identify key insights.")

# displaying key metrics

col1, col2, col3 = st.columns(3)
with col1:
  total_volume = int(df["Traffic Volume"].sum())
  st.metric(label = "Total Traffic volume", value = f"{total_volume:,}", border = True)

with col2:
  avg_speed = int(df["Average Speed"].mean())
  st.metric(label = "Average Speed (km/h)",value = f"{avg_speed:,} km/h", border = True)

with col3:
  avg_congestion = int(df["Congestion Level"].mean())
  st.metric(label = "Average Congestion", value = f"{avg_congestion:,}%", border = True)

tab1, tab2, tab3, tab4, tab5 = st.tabs([
                            "High Traffic Volume Roads",
                            "Daily Traffic Volume",
                            "Weather Impact",
                            "Public Transport Impact",
                            "Monthly/Yearly Trends",
                          ])

# TAB 1

# this is for "High Traffic Volume"
with tab1:
  st.subheader("High Traffic Volume Roads")

  # calculating congestion level and avg speed based on the "Area Name" and "Road/Intersection Name"
  avg_speed_congestion = df.groupby(["Area Name", "Road/Intersection Name"]).agg({
    "Traffic Volume": 'mean',
    "Average Speed": 'mean',
    "Congestion Level": 'mean'
  }).reset_index()

  sorted_speed_congestion = avg_speed_congestion.sort_values(by = ["Congestion Level", "Average Speed"], ascending = [False, True])

  # Adding the slide bar
  high_traffic_radio = st.radio(
    "Select the number of top roads to display",
    options = [
      "All",
      "Top 3",
      "Top 5",
      "Top 10"
    ],
    horizontal = True
  )

  if high_traffic_radio == "Top 3":
    plot_traffic_volume = sorted_speed_congestion.head(3)
  elif high_traffic_radio == "Top 5":
    plot_traffic_volume = sorted_speed_congestion.head(5)
  elif high_traffic_radio == "Top 10":
    plot_traffic_volume = sorted_speed_congestion.head(10)
  else:
    plot_traffic_volume = sorted_speed_congestion

  # Plotting
  fig = px.bar(plot_traffic_volume, x = "Road/Intersection Name", y = "Traffic Volume", color = "Congestion Level", title = f"{high_traffic_radio} roads with High Traffic Volume, Low Average Speed and High Congestion Level")
  st.plotly_chart(fig, use_container_width = True)

# TAB 2

# this for "Daily Traffic Volume"
with tab2:
  # Traffic patterns for the selected road/intersection
  st.subheader("Daily Traffic Volume")

  filter_col, graph_col = st.columns([1, 2])

  with filter_col:
    selected_road = None

    selected_area = st.selectbox(
      "Select Area Name:",
      options = df["Area Name"].unique(),
      index = None,
      placeholder = "Select Area Name",
      key = "area_selector"
    )

    if selected_area:
      filtered_road_names = df[df["Area Name"] == selected_area]["Road/Intersection Name"].unique()

      selected_road = st.selectbox(
        "Select Road/Intersection Name:",
        options = filtered_road_names,
        index = None,
        placeholder = "Select Road/Intersection Name",
        key = "road_selector"
      )

      st.write("You Selected:", selected_area, ",", selected_road)

  with graph_col:
    if selected_road:
        filtered_df = df[df["Road/Intersection Name"] == selected_road]

        daily_traffic = filtered_df.groupby(["Day Name", "Day of Week"])["Traffic Volume"].mean().reset_index()

        # fig, ax = plt.subplots(figsize = (12, 6))
        fig = px.line(daily_traffic.sort_values(by = "Day of Week"), x = "Day Name", y = "Traffic Volume", title = f"Daily Traffic Volume for {selected_road} in {selected_area}")
        st.plotly_chart(fig, use_container_width = True)

    else:
      st.info("👈 Please select the Area and Road/Intersection to view the daily traffic volume.")

# TAB 3

# this is for "Weather Impact"
with tab3:
  st.subheader("Weather impact on Traffic Volume")

  avg_traffic_weather = df.groupby(["Day Name", "Day of Week", "Weather Conditions"]).agg({
    "Traffic Volume": "mean",
    "Average Speed": "mean"
  }).reset_index()

  avg_traffic_weather_day = avg_traffic_weather.sort_values(by = "Day of Week")

  weather_radio = st.radio(
    "Select the Weather Condition to see the impact on Traffic and Speed",
    options = [
      "All",
      "Clear",
      "Overcast",
      "Fog",
      "Rain",
      "Windy"
    ],
    horizontal = True
  )

  weather_plot = df
  plot_title = ""

  if weather_radio == "All":
    weather_plot = avg_traffic_weather_day
    plot_title = "Overall Weather impact on Traffic and Speed"
  else:
    weather_plot = avg_traffic_weather_day[avg_traffic_weather_day["Weather Conditions"] == weather_radio]
    plot_title = f"Traffic and Speed during {weather_radio} weather"

  if weather_plot is not None:

    col1, col2 = st.columns(2)

    with col1:
      fig1 = px.line(weather_plot,
                    x = "Day Name",
                    y = "Traffic Volume",
                    color = "Weather Conditions" if weather_radio == "All" else None,
                    title = f"Traffic Volume on {weather_radio} Day")
      st.plotly_chart(fig1, use_container_width = True)
    
    with col2:
      fig2 = px.line(weather_plot,
                    x = "Day Name",
                    y = "Average Speed",
                    color = "Weather Conditions" if weather_radio == "All" else None,
                    title = f"Average Speed on {weather_radio} Day")
      st.plotly_chart(fig2, use_container_width = True)

# TAB 4

# this is for "Public Transport Impact"
with tab4:
  st.subheader("Public Transport Impact on Traffic and Speed")

  bins = [0, 25, 50, 75, 100]
  labels = ["Low Use", "Medium Low Use", "Medium High Use", "High Use"]

  df["Public Transport Bins"] = pd.cut(df["Public Transport Usage"], bins = bins, labels = labels, right = False)

  # st.write(Public_Transport_Bins.value_counts())

  avg_by_transport = df.groupby("Public Transport Bins").agg({
    "Traffic Volume": "mean",
    "Average Speed": "mean"
  }).reset_index()

  traffic_speed_radio = st.radio(
    "Select a metric to view the impact",
    options = [
      "Traffic Volume",
      "Average Speed"
    ],
    horizontal = True
  )

  if traffic_speed_radio == "Traffic Volume":
    fig = px.bar(avg_by_transport, x = "Public Transport Bins", y = "Traffic Volume", title = "Impact of Public Transport Usage on Traffic Volume")
    st.plotly_chart(fig, use_container_width = True)
  else:
    fig = px.bar(avg_by_transport, x = "Public Transport Bins", y = "Average Speed", title = "Average Speed by Public Transport Usage")
    st.plotly_chart(fig, use_container_width = True)

# TAB 5

# this is for "Monthly/Yearly Trends"
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month Number'] = df['Date'].dt.month
df['Month Name'] = df['Date'].dt.month_name()

with tab5:
  st.subheader("Monthly and Yearly Traffic Trends")
  years = df["Year"].unique()
  # months = df["Month"].unique()

  col_years, col_months = st.columns(2)

  with col_years:
    selected_year = st.selectbox(
      "Select a year",
      options = sorted(years),
      index = None,
      placeholder = "Select a Year"
    )

  with col_months:
    if selected_year:
      months_in_year = df[df['Year'] == selected_year]['Month Name'].unique()
      selected_month = st.selectbox(
        "Select a Month",
        options = months_in_year,
        index = None,
        placeholder = "Select a Month"
      )
    else:
      selected_month = None

  if selected_year and selected_month:
    filtered_year_month = df[(df["Year"] == selected_year) & (df["Month Name"] == selected_month)]
    # monthly_avg = filtered_year_month.groupby("Month Name")["Traffic Volume"].mean().reset_index()
    # monthly_avg_speed = filtered_year_month.groupby("Month Name")["Average Speed"].mean().reset_index()

    if not filtered_year_month.empty:
      fig = px.bar(filtered_year_month,
                    x = "Date",
                    y = "Traffic Volume",
                    title = f"Traffic Volume in {selected_month} {selected_year}")
      fig.update_xaxes(title_text = "Month")
      fig.update_yaxes(title_text = "Traffic Volume")
      st.plotly_chart(fig, use_container_width = True)
    else:
      st.info("No data available for the selected time period.")
  else:
    st.info("Please select a Year and a Month to view the trends.")