
from diagrams import Diagram, Cluster

from diagrams.aws.management import Organizations, OrganizationsAccount, OrganizationsOrganizationalUnit
from diagrams.aws.general import Users, User

with Diagram("SSO-State", show=False, direction="TB"):
    gg = Users("Group")
    uu= User("User")

    with Cluster('Groups'):

        gg_0= Users("AWSSecurityAudit\nPowerUsers")

        with Cluster("SecOps_Adms"):

                gg_1= [User("w.alejovl+secops\n-labs@gmail.com"),]

        gg_2= Users("AWSServiceCatalo\ngAdmins")

        with Cluster("AWSControlTowerAdmins"):

                gg_3= [User("velez94@protonma\nil.com"),]

        with Cluster("AWSAccountFactory"):

                gg_4= [User("velez94@protonma\nil.com"),]

        with Cluster("DevSecOps_Admins"):

                gg_5= [User("DevSecOpsAdm"),]

        gg_6= Users("AWSLogArchiveAdm\nins")

        gg_7= Users("AWSLogArchiveVie\nwers")

        gg_8= Users("AWSSecurityAudit\nors")
