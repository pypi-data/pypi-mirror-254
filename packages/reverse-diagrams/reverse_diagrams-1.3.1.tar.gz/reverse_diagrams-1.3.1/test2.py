import boto3

import logging

profile = "labvel-master"
boto3.setup_default_session(profile_name=profile)


def list_groups_pag(identity_store_id,client=boto3.client('identitystore', region_name="us-east-2"), next_token: str = None):
    paginator = client.get_paginator('list_groups')
    response_iterator = paginator.paginate(
        IdentityStoreId=identity_store_id,
        PaginationConfig={
            'MaxItems': 1000,
            'PageSize': 4,
            'StartingToken': next_token
        }
    )
    response = response_iterator.build_full_result()
    logging.info(response_iterator.build_full_result())
    return response["Groups"]


def list_groups(identity_store_id, client=boto3.client('identitystore', region_name="us-east-2"), ):
    groups = client.list_groups(
        IdentityStoreId=identity_store_id,
        MaxResults = 2
    )

    logging.info(groups)
    l_groups = groups["Groups"]
    logging.info(len(groups["Groups"]))

    if len(groups["Groups"]) >= 2:
        logging.info("Paginating ...")
        ad_groups = list_groups_pag(identity_store_id=identity_store_id,client= client, next_token=groups["NextToken"])
        for ad in ad_groups:
            l_groups.append(ad)
        logging.info(f"You have {len(l_groups)} Groups")
    print(len(l_groups))
    return l_groups


list_groups(identity_store_id="d-9a672b3314")
