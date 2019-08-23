import pandas as pd
import os, sys
import pdb
import matplotlib.pyplot as plt


def extract_gt(csvs_path, data, plot):
	for csv_file in os.listdir(csvs_path):
		if csv_file.endswith(data + ".csv"):
			dataframe = pd.read_csv(csvs_path + "/" + csv_file)

			if data == "pose_estimate":
				pos_x = dataframe['.pose.pose.position.x']
				pos_y = dataframe['.pose.pose.position.y']
				pos_z = dataframe['.pose.pose.position.z']
				quat_x = dataframe['.pose.pose.orientation.x']
				quat_y = dataframe['.pose.pose.orientation.y']
				quat_z = dataframe['.pose.pose.orientation.z']
				quat_w = dataframe['.pose.pose.orientation.w']
				lin_vel_x = dataframe['.twist.twist.linear.x']
				lin_vel_y = dataframe['.twist.twist.linear.y']
				lin_vel_z = dataframe['.twist.twist.linear.z']
				ang_vel_x = dataframe['.twist.twist.angular.x']
				ang_vel_y = dataframe['.twist.twist.angular.y']
				ang_vel_z = dataframe['.twist.twist.angular.z']
				plt.plot(pos_z)

			if data == "target_status":
				status = dataframe['.data']

			if data == "rateThrust":
				u_angrate_x = dataframe['.angular_rates.x']
				u_angrate_y = dataframe['.angular_rates.y']
				u_angrate_z = dataframe['.angular_rates.z']
				u_thrust_z = dataframe['.thrust.z']

			if data == "imu":
				ang_vel_x = dataframe['.angular_velocity.x']
				ang_vel_y = dataframe['.angular_velocity.y']
				ang_vel_z = dataframe['.angular_velocity.z']
				lin_acc_x = dataframe['.linear_acceleration.x']
				lin_acc_y = dataframe['.linear_acceleration.y']
				lin_acc_z = dataframe['.linear_acceleration.z']
				# plt.plot(ang_vel_x)
				# plt.show()

			if data == "velocity_estimate":
				lin_vel_x = dataframe['.twist.linear.x']
				lin_vel_y = dataframe['.twist.linear.y']
				lin_vel_z = dataframe['.twist.linear.z']
				# plt.plot(lin_vel_x)
				# plt.show()
	plt.show()


if __name__ == '__main__':
	data_folder = "1_6e7"
	data = "pose_estimate"
	# data = "target_status"
	# data = "rateThrust"
	# data = "imu"
	# data = "velocity_estimate"

	csvs_path = "/home/klee698/rosbag_ws/src/rosbag_to_csv/csvs/" + data_folder
	extract_gt(csvs_path, data, plot=True)
