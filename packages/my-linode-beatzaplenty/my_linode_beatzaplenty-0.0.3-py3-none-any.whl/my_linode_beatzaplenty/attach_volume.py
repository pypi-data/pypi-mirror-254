def attach_volume(api_client, volume_label, instance):
    """
    Attach Persistent volume to Linode Instance

    :param api_client: A linode_api4.client object to connect to Linode
    :param volume_label: Label of the target volume
    :param instance: A linode_api4.instance object representing the linode instance to attach the volume to
    """
    # Find the volume by label
    volumes = api_client.volumes()
    for volume in volumes:
        if volume.label == volume_label:
            datavol = volume
    if not datavol:
        print(f"Volume with label '{volume_label}' not found.")
        return

    # Attach the volume to the Linode instance
    datavol.attach(instance.id)
    
    print(f"Volume '{volume_label}' attached to Linode instance {instance.id}.")


if __name__ == "__main__":
    import argparse
    from linode_api4 import LinodeClient, Instance

    parser=argparse.ArgumentParser()

    parser.add_argument("--api_client", help="A linode_api4.client object used to run the command",required=True,type=LinodeClient)
    parser.add_argument("--label", help="The Volume Label",required=True, type=str)
    parser.add_argument("--instance", help="The linode instance to attache the volume to. Must be a linode_api4.instance object",required=True, type=Instance)

    args=parser.parse_args()

    attach_volume(api_client=args.api_client,volume_label=args.label,instance=args.instance)