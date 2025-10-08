#!/usr/bin/env python3
# This is the local test client script for the ManipulationNet benchmark: manipulation-net.org
# You can experience the same task protocol locally.
# DO NOT MODIFY THIS FILE
# Contact: support@manipulation-net.org


try:
    import rospy
    from mnet_client.clients import LocalTestClient
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Please ensure all required modules are installed and properly configured.")
    exit()


if __name__ == "__main__":
    """
    Main function to run the local test client
    """
    try:
        client = LocalTestClient()
        client.run()
    except rospy.ROSInterruptException:
        pass
