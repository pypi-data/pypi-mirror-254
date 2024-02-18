def get_stackscript_id_by_label_and_username(api_client, stackscript_label, stackscript_username):
    import linode_api4
    """
    Get the ID of a StackScript based on its label and username.

    :param api_client: The linode_api4.Api object to use for making API calls.
    :param stackscript_label: The label of the StackScript.
    :param stackscript_username: The username associated with the StackScript.
    :return: The ID of the StackScript, or None if not found.
    """
    try:
        # Retrieve StackScripts
        obj = linode_api4.linode.StackScript
        stackscripts = api_client.linode.stackscripts(linode_api4.linode.StackScript.mine==True)

        # Find the StackScript with the specified label and username
        matching_stackscript = next(
            (script for script in stackscripts if script.label == stackscript_label and script.username == stackscript_username),
            None
        )

        if matching_stackscript:
            # Return the ID of the matching StackScript
            return matching_stackscript.id
        else:
            print(f"StackScript with label '{stackscript_label}' and username '{stackscript_username}' not found.")
            return None
    except linode_api4.ApiError as e:
        # Display error message
        print(f"Error retrieving StackScripts: {e}")
        return None
if __name__ == "__main__":
    import argparse
    from linode_api4 import LinodeClient

    parser=argparse.ArgumentParser()

    parser.add_argument("--api_client", help="The linode api client to connect to linode with.",required=True, type=LinodeClient)
    parser.add_argument("--label", help="The stackscript label to search on",required=True, type=str)
    parser.add_argument("--username", help="The linode username to search on",required=True, type=str)
    
    args=parser.parse_args()
    get_stackscript_id_by_label_and_username(api_client=args.api_client,
                                             stackscript_label=args.label,
                                             stackscript_username=args.username)