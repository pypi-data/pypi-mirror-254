def detach_all_volumes(instance):
    """
    Detach all persistent volumes from Linode Instance

    :param instance: A linode_api4.instance object representing the linode instance to detach all volumes from
    """
    # Get a list of attached volumes
    attached_volumes = instance.volumes()

    if not attached_volumes:
        print(f"No volumes attached to Linode instance {instance.id}.")
        return

    # Detach each attached volume
    for volume in attached_volumes:
        volume.detach()
        print(f"Volume {volume.id} detached from Linode instance {instance.id}.")
if __name__ == "__main__":
    import argparse
    from linode_api4 import Instance

    parser=argparse.ArgumentParser()

    parser.add_argument("--instance", help="The linode instance to detach volumes from",required=True, type=Instance)
    
    args=parser.parse_args()
    detach_all_volumes(args.instance)