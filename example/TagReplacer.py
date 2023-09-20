def processTags(aws_access_key_id, aws_secret_access_key, aws_session_token, region, plan=True):
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token,
        region_name=region
    ) 

    # Create a ResourceGroupsTaggingAPI client named 'tag_api'
    tag_api = session.client("resourcegroupstaggingapi")

    # list all tagged resources
    paginator = tag_api.get_paginator("get_resources")

    # Traverse resources and find resources containing the 'project' tag, and create new tags to replace the original non-standard tags.
    for page in paginator.paginate():
        for resource in page['ResourceTagMappingList']:
            resource_arn = resource['ResourceARN']
            strarn=f"Resource ARN: {resource_arn}"

            project_value = ""
            pcn_finance_project_exist = False

            for tag in resource['Tags']:
                key_no_space_lower = tag['Key'].replace(" ", "").lower()
                if key_no_space_lower == "project":
                    project_value = tag['Value']
                    stroriginal=f"Original Project Tag: {tag['Key']}={tag['Value']}"
                elif key_no_space_lower == "pcn:finance:project":
                    pcn_finance_project_exist = True

            if project_value and not pcn_finance_project_exist:
                print(strarn)
                print(stroriginal)
                resource_type, resource_id = get_resource_info(resource_arn)
                if plan:
                    print(f"Plan to add tag: pcn:finance:project={project_value}\n")
                else:
                    add_new_tag(tag_api, resource_arn, "pcn:finance:project", project_value)
                    resource_type, resource_id = get_resource_info(resource_arn)
                    print(f"Added 'pcn:finance:project' tag with value: {project_value} for Resource Type: {resource_type} and Resource Identifier: {resource_id}\n")