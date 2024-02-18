def get_firewall_id_by_label(api_client, firewall_label):
    import linode_api4
    """
    Get the ID of a firewall based on its label.

    :param api_client: The linode_api4.Api object to use for making API calls.
    :param firewall_label: The label of the firewall.
    :return: The ID of the firewall, or None if not found.
    """
    try:
        # Retrieve firewalls
        firewalls = api_client.networking.firewalls()

        # Find the firewall with the specified label
        matching_firewall = next((fw for fw in firewalls if fw.label == firewall_label), None)

        if matching_firewall:
            # Return the ID of the matching firewall
            return matching_firewall.id
        else:
            print(f"Firewall with label '{firewall_label}' not found.")
            return None
    except linode_api4.ApiError as e:
        # Display error message
        print(f"Error retrieving firewalls: {e}")
        return None
    
if __name__ == "__main__":
    import argparse
    from linode_api4 import LinodeClient

    parser=argparse.ArgumentParser()

    parser.add_argument("--api_client", help="The linode api client to connect to linode with.",required=True, type=LinodeClient)
    parser.add_argument("--label", help="The firewall label to search on",required=True, type=str)
    
    args=parser.parse_args()

    get_firewall_id_by_label(api_client=args.api_client,firewall_label=args.label)