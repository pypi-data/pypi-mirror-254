def get_ssh_key_id_by_label(api_client, ssh_key_label):
    import linode_api4
    """
    Get the ID of an SSH key based on its label.

    :param api_client: The linode_api4.Api object to use for making API calls.
    :param ssh_key_label: The label of the SSH key.
    :return: The ID of the SSH key, or None if not found.
    """
    try:
        # Retrieve SSH keys
        ssh_keys = api_client.profile.ssh_keys()

        # Find the SSH key with the specified label
        matching_ssh_key = next((key for key in ssh_keys if key.label == ssh_key_label), None)

        if matching_ssh_key:
            # Return the ID of the matching SSH key
            return matching_ssh_key.id
        else:
            print(f"SSH key with label '{ssh_key_label}' not found.")
            return None
    except linode_api4.ApiError as e:
        # Display error message
        print(f"Error retrieving SSH keys: {e}")
        return None
    
if __name__ == "__main__":
    import argparse
    from linode_api4 import LinodeClient

    parser=argparse.ArgumentParser()

    parser.add_argument("--api_client", help="The linode api client to connect to linode with.",required=True, type=LinodeClient)
    parser.add_argument("--label", help="The SSH Key label to search on",required=True, type=str)
    
    args=parser.parse_args()
    get_ssh_key_id_by_label(api_client=args.api_client,ssh_key_label=args.label)