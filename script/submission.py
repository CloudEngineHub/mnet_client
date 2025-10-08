#!/usr/bin/env python3
# This is the client script for the ManipulationNet benchmark: manipulation-net.org
# It is used to record and send the performance video to the server
# DO NOT MODIFY THIS FILE
# Contact: support@manipulation-net.org

try:
    import rospy
    from mnet_client.clients import SubmissionClient
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Please ensure all required modules are installed and properly configured.")
    exit()


if __name__ == "__main__":
    try:
        client = SubmissionClient()
        client.run()
    except rospy.ROSInterruptException:
        pass
