import psycopg2
from config import config


def insert_ci(ci_name):
    """ insert a new vendor into the CI table """
    sql = 'INSERT INTO public."CI_Table"(ci_name) VALUES(%s)'
    conn = None
    idCI = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (ci_name,))
        # get the generated id back
        idCI = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_ci_list(ci_List):
    """ insert multiple CI's into the CI table  """
    sql = 'INSERT INTO "TPFinal"."CI_Table"("idCi","ciName","ciBrand","ciModel","ciLocationID","ciClassID","ciPurchaseDate","ciStatusID") VALUES(default,%s, %s, %s,%s, %s, %s,%s)'
    conn = None
    try:
        # read database configuration
        params = config('', 'CEIoT')
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,ci_List)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_ci_topology_list(ci_List):
    """ insert multiple CI's into the CI Topology (neigbor) table  """
    sql = 'INSERT INTO "TPFinal"."CI_Topology"("timestamp","ciID","neighborID") VALUES(%s, %s, %s)'
    conn = None
    try:
        # read database configuration
        params = config('', 'POSTGRES')
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,ci_List)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_ci_location_list(location_List):
    """ insert multiple vendors into the CI Locations table  """
    sql = 'INSERT INTO public."CI_Locations"(location_name, location_latitud, location_longitud) VALUES(%s, %s, %s)'
    conn = None
    try:
        # read database configuration
        params = config('', 'POSTGRES')
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,location_List)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_list(List):
    """ insert multiple vendors into the CI Locations table  """
    sql = 'INSERT INTO "Ventas"."Productos"() VALUES(%s, %s, %s)'
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,location_List)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    ci_table_list=[('useast1-dcc-002','Juniper','MX480',1,3,"12/12/2020",1),
    ('useast1-dcd-001','Juniper','VCF 2500',1,4,"12/12/2020",1),
    ('useast1-dcd-002','Juniper','VCF 2500',1,4,"12/12/2020",1),
    ('useast1-dcd-003','Juniper','VCF 2500',1,4,"12/12/2020",1),
    ('useast1-dcd-004','Juniper','VCF 2500',1,4,"12/12/2020",1),
    ('useast1-dcd-005','Juniper','VCF 2500',1,4,"12/12/2020",1),
    ('useast1-dcd-006','Juniper','VCF 2500',1,4,"12/12/2020",1),
    ('useast1-dcd-101','Juniper','VCF 1100',1,4,"12/12/2020",1),
    ('useast1-dcd-102','Juniper','VCF 1100',1,4,"12/12/2020",1),
    ('useast1-dcd-103','Juniper','VCF 1100',1,4,"12/12/2020",1),
    ('useast1-dcd-104','Juniper','VCF 1100',1,4,"12/12/2020",1),
    ('useast1-dcd-105','Juniper','VCF 1100',1,4,"12/12/2020",1),
    ('useast1-dcd-106','Juniper','VCF 1100',1,4,"12/12/2020",1),
    ('useast1-dcd-107','Juniper','VCF 1100',1,4,"12/12/2020",1),
    ('useast1-dcd-108','Juniper','VCF 1100',1,4,"12/12/2020",1),
    ('useast1-dcd-109','Juniper','VCF 1100',1,4,"12/12/2020",1),
    ('useast1-dcd-110','Juniper','VCF 1100',1,4,"12/12/2020",1),
    ('useast1-dcd-111','Juniper','VCF 1100',1,4,"12/12/2020",1),
    ('useast1-dcd-112','Juniper','VCF 1100',1,4,"12/12/2020",1),
    ('useast1-dcd-113','Juniper','VCF 1100',1,4,"12/12/2020",1),
    ('useast1-dcd-114','Juniper','VCF 1100',1,4,"12/12/2020",1),
    ('useast1-dcd-115','Juniper','VCF 1100',1,4,"12/12/2020",1),
    ('useast1-dcd-116','Juniper','VCF 1100',1,4,"12/12/2020",1),
    ('useast1-dcd-117','Juniper','VCF 1100',1,4,"12/12/2020",1),
    ('useast1-dcd-118','Juniper','VCF 1100',1,4,"12/12/2020",1),
    ('useast1-tor-001','Cisco','Catalyst 9300',1,4,"12/12/2020",1),
    ('useast1-tor-002','Cisco','Catalyst 9300',1,4,"12/12/2020",1),
    ('useast1-tor-003','Cisco','Catalyst 9300',1,4,"12/12/2020",1),
    ('useast1-tor-004','Cisco','Catalyst 9300',1,4,"12/12/2020",1),
    ('useast1-tor-005','Cisco','Catalyst 9300',1,4,"12/12/2020",1),
    ('useast1-tor-006','Cisco','Catalyst 9300',1,4,"12/12/2020",1),
    ('useast1-tor-007','Cisco','Catalyst 9300',1,4,"12/12/2020",1),
    ('useast1-tor-008','Cisco','Catalyst 9300',1,4,"12/12/2020",1),
    ('useast1-tor-009','Cisco','Catalyst 9300',1,4,"12/12/2020",1),
    ('useast1-tor-010','Cisco','Catalyst 9300',1,4,"12/12/2020",1),
    ('useast1-boa-001','Cisco','Catalyst 3750',1,4,"12/12/2020",1),
    ('useast1-boa-002','Cisco','Catalyst 3750',1,4,"12/12/2020",1),
    ('useast1-boa-003','Cisco','Catalyst 3750',1,4,"12/12/2020",1),
    ('useast1-boa-004','Cisco','Catalyst 3750',1,4,"12/12/2020",1),
    ('useast1-boa-005','Cisco','Catalyst 3750',1,4,"12/12/2020",1),
    ('useast1-boa-006','Cisco','Catalyst 3750',1,4,"12/12/2020",1),
    ('useast1-boa-007','Cisco','Catalyst 3750',1,4,"12/12/2020",1),
    ('useast1-boa-008','Cisco','Catalyst 3750',1,4,"12/12/2020",1),
    ('useast1-boa-009','Cisco','Catalyst 3750',1,4,"12/12/2020",1),
    ('useast1-boa-010','Cisco','Catalyst 3750',1,4,"12/12/2020",1),
    ('useast1-boa-011','Cisco','Catalyst 3750',1,4,"12/12/2020",1),
    ('useast1-boa-012','Cisco','Catalyst 3750',1,4,"12/12/2020",1),
    ('useast1-win-001','Dell','r710',1,1,"12/12/2020",1),
    ('useast1-win-002','Dell','r710',1,1,"12/12/2020",1),
    ('useast1-win-003','Dell','r710',1,1,"12/12/2020",1),
    ('useast1-win-004','Dell','r710',1,1,"12/12/2020",1),
    ('useast1-win-005','Dell','r710',1,1,"12/12/2020",1),
    ('useast1-lin-001','Dell','r710',1,2,"12/12/2020",1),
    ('useast1-lin-002','Dell','r710',1,2,"12/12/2020",1),
    ('useast1-lin-003','Dell','r710',1,2,"12/12/2020",1),
    ('useast1-lin-004','Dell','r710',1,2,"12/12/2020",1),
    ('useast1-lin-005','Dell','r710',1,2,"12/12/2020",1),
    ('useast1-phx-001','Cisco','VoicePhone',1,5,"12/12/2020",1),
    ('useast1-prn-001','HP','LaserJet 100',1,5,"12/12/2020",1),
    ('uswest1-dcc-001','Juniper','MX480',2,3,"12/12/2020",1),
    ('uswest1-dcc-002','Juniper','MX480',2,3,"12/12/2020",1),
    ('uswest1-dcd-001','Juniper','VCF 2500',2,4,"12/12/2020",1),
    ('uswest1-dcd-002','Juniper','VCF 2500',2,4,"12/12/2020",1),
    ('uswest1-dcd-003','Juniper','VCF 2500',2,4,"12/12/2020",1),
    ('uswest1-dcd-004','Juniper','VCF 2500',2,4,"12/12/2020",1),
    ('uswest1-dcd-005','Juniper','VCF 2500',2,4,"12/12/2020",1),
    ('uswest1-dcd-006','Juniper','VCF 2500',2,4,"12/12/2020",1),
    ('uswest1-dcd-101','Juniper','VCF 1100',2,4,"12/12/2020",1),
    ('uswest1-dcd-102','Juniper','VCF 1100',2,4,"12/12/2020",1),
    ('uswest1-dcd-103','Juniper','VCF 1100',2,4,"12/12/2020",1),
    ('uswest1-dcd-104','Juniper','VCF 1100',2,4,"12/12/2020",1),
    ('uswest1-dcd-105','Juniper','VCF 1100',2,4,"12/12/2020",1),
    ('uswest1-dcd-106','Juniper','VCF 1100',2,4,"12/12/2020",1),
    ('uswest1-dcd-107','Juniper','VCF 1100',2,4,"12/12/2020",1),
    ('uswest1-dcd-108','Juniper','VCF 1100',2,4,"12/12/2020",1),
    ('uswest1-dcd-109','Juniper','VCF 1100',2,4,"12/12/2020",1),
    ('uswest1-dcd-110','Juniper','VCF 1100',2,4,"12/12/2020",1),
    ('uswest1-dcd-111','Juniper','VCF 1100',2,4,"12/12/2020",1),
    ('uswest1-dcd-112','Juniper','VCF 1100',2,4,"12/12/2020",1),
    ('uswest1-dcd-113','Juniper','VCF 1100',2,4,"12/12/2020",1),
    ('uswest1-dcd-114','Juniper','VCF 1100',2,4,"12/12/2020",1),
    ('uswest1-dcd-115','Juniper','VCF 1100',2,4,"12/12/2020",1),
    ('uswest1-dcd-116','Juniper','VCF 1100',2,4,"12/12/2020",1),
    ('uswest1-dcd-117','Juniper','VCF 1100',2,4,"12/12/2020",1),
    ('uswest1-dcd-118','Juniper','VCF 1100',2,4,"12/12/2020",1),
    ('uswest1-tor-001','Cisco','Catalyst 9300',2,4,"12/12/2020",1),
    ('uswest1-tor-002','Cisco','Catalyst 9300',2,4,"12/12/2020",1),
    ('uswest1-tor-003','Cisco','Catalyst 9300',2,4,"12/12/2020",1),
    ('uswest1-tor-004','Cisco','Catalyst 9300',2,4,"12/12/2020",1),
    ('uswest1-tor-005','Cisco','Catalyst 9300',2,4,"12/12/2020",1),
    ('uswest1-tor-006','Cisco','Catalyst 9300',2,4,"12/12/2020",1),
    ('uswest1-tor-007','Cisco','Catalyst 9300',2,4,"12/12/2020",1),
    ('uswest1-tor-008','Cisco','Catalyst 9300',2,4,"12/12/2020",1),
    ('uswest1-tor-009','Cisco','Catalyst 9300',2,4,"12/12/2020",1),
    ('uswest1-tor-010','Cisco','Catalyst 9300',2,4,"12/12/2020",1),
    ('uswest1-boa-001','Cisco','Catalyst 3750',2,4,"12/12/2020",1),
    ('uswest1-boa-002','Cisco','Catalyst 3750',2,4,"12/12/2020",1),
    ('uswest1-boa-003','Cisco','Catalyst 3750',2,4,"12/12/2020",1),
    ('uswest1-boa-004','Cisco','Catalyst 3750',2,4,"12/12/2020",1),
    ('uswest1-boa-005','Cisco','Catalyst 3750',2,4,"12/12/2020",1),
    ('uswest1-boa-006','Cisco','Catalyst 3750',2,4,"12/12/2020",1),
    ('uswest1-boa-007','Cisco','Catalyst 3750',2,4,"12/12/2020",1),
    ('uswest1-boa-008','Cisco','Catalyst 3750',2,4,"12/12/2020",1),
    ('uswest1-boa-009','Cisco','Catalyst 3750',2,4,"12/12/2020",1),
    ('uswest1-boa-010','Cisco','Catalyst 3750',2,4,"12/12/2020",1),
    ('uswest1-boa-011','Cisco','Catalyst 3750',2,4,"12/12/2020",1),
    ('uswest1-boa-012','Cisco','Catalyst 3750',2,4,"12/12/2020",1),
    ('uswest1-win-001','Dell','r710',2,1,"12/12/2020",1),
    ('uswest1-win-002','Dell','r710',2,1,"12/12/2020",1),
    ('uswest1-win-003','Dell','r710',2,1,"12/12/2020",1),
    ('uswest1-win-004','Dell','r710',2,1,"12/12/2020",1),
    ('uswest1-win-005','Dell','r710',2,1,"12/12/2020",1),
    ('uswest1-lin-001','Dell','r710',2,2,"12/12/2020",1),
    ('uswest1-lin-002','Dell','r710',2,2,"12/12/2020",1),
    ('uswest1-lin-003','Dell','r710',2,2,"12/12/2020",1),
    ('uswest1-lin-004','Dell','r710',2,2,"12/12/2020",1),
    ('uswest1-lin-005','Dell','r710',2,2,"12/12/2020",1),
    ('uswest1-phx-001','Cisco','VoicePhone',2,5,"12/12/2020",1),
    ('uswest1-prn-001','HP','LaserJet 100',2,5,"12/12/2020",1),
    ('eusouth1-dcc-001','Juniper','MX480',4,3,"12/12/2020",1),
    ('eusouth1-dcd-001','Juniper','VCF 2500',4,4,"12/12/2020",1),
    ('eusouth1-dcd-002','Juniper','VCF 2500',4,4,"12/12/2020",1),
    ('eusouth1-dcd-003','Juniper','VCF 2500',4,4,"12/12/2020",1),
    ('eusouth1-dcd-101','Juniper','VCF 1100',4,4,"12/12/2020",1),
    ('eusouth1-dcd-102','Juniper','VCF 1100',4,4,"12/12/2020",1),
    ('eusouth1-dcd-103','Juniper','VCF 1100',4,4,"12/12/2020",1),
    ('eusouth1-dcd-104','Juniper','VCF 1100',4,4,"12/12/2020",1),
    ('eusouth1-dcd-105','Juniper','VCF 1100',4,4,"12/12/2020",1),
    ('eusouth1-dcd-106','Juniper','VCF 1100',4,4,"12/12/2020",1),
    ('eusouth1-dcd-107','Juniper','VCF 1100',4,4,"12/12/2020",1),
    ('eusouth1-dcd-108','Juniper','VCF 1100',4,4,"12/12/2020",1),
    ('eusouth1-dcd-109','Juniper','VCF 1100',4,4,"12/12/2020",1),
    ('eusouth1-tor-001','Cisco','Catalyst 9300',4,4,"12/12/2020",1),
    ('eusouth1-tor-002','Cisco','Catalyst 9300',4,4,"12/12/2020",1),
    ('eusouth1-tor-003','Cisco','Catalyst 9300',4,4,"12/12/2020",1),
    ('eusouth1-tor-004','Cisco','Catalyst 9300',4,4,"12/12/2020",1),
    ('eusouth1-tor-005','Cisco','Catalyst 9300',4,4,"12/12/2020",1),
    ('eusouth1-tor-006','Cisco','Catalyst 9300',4,4,"12/12/2020",1),
    ('eusouth1-tor-007','Cisco','Catalyst 9300',4,4,"12/12/2020",5),
    ('eusouth1-tor-008','Cisco','Catalyst 9300',4,4,"12/12/2020",5),
    ('eusouth1-tor-009','Cisco','Catalyst 9300',4,4,"12/12/2020",5),
    ('eusouth1-tor-010','Cisco','Catalyst 9300',4,4,"12/12/2020",5),
    ('eusouth1-boa-001','Cisco','Catalyst 3750',4,4,"12/12/2020",1),
    ('eusouth1-boa-002','Cisco','Catalyst 3750',4,4,"12/12/2020",1),
    ('eusouth1-boa-003','Cisco','Catalyst 3750',4,4,"12/12/2020",1),
    ('eusouth1-boa-004','Cisco','Catalyst 3750',4,4,"12/12/2020",1),
    ('eusouth1-boa-005','Cisco','Catalyst 3750',4,4,"12/12/2020",1),
    ('eusouth1-boa-006','Cisco','Catalyst 3750',4,4,"12/12/2020",5),
    ('eusouth1-boa-007','Cisco','Catalyst 3750',4,4,"12/12/2020",5),
    ('eusouth1-boa-008','Cisco','Catalyst 3750',4,4,"12/12/2020",5),
    ('eusouth1-boa-009','Cisco','Catalyst 3750',4,4,"12/12/2020",5),
    ('eusouth1-boa-010','Cisco','Catalyst 3750',4,4,"12/12/2020",5),
    ('eusouth1-boa-011','Cisco','Catalyst 3750',4,4,"12/12/2020",5),
    ('eusouth1-boa-012','Cisco','Catalyst 3750',4,4,"12/12/2020",5),
    ('eusouth1-win-001','Dell','r710',4,1,"12/12/2020",1),
    ('eusouth1-win-002','Dell','r710',4,1,"12/12/2020",1),
    ('eusouth1-win-003','Dell','r710',4,1,"12/12/2020",1),
    ('eusouth1-win-004','Dell','r710',4,1,"12/12/2020",5),
    ('eusouth1-win-005','Dell','r710',4,1,"12/12/2020",5),
    ('eusouth1-lin-001','Dell','r710',4,2,"12/12/2020",1),
    ('eusouth1-lin-002','Dell','r710',4,2,"12/12/2020",1),
    ('eusouth1-lin-003','Dell','r710',4,2,"12/12/2020",1),
    ('eusouth1-lin-004','Dell','r710',4,2,"12/12/2020",5),
    ('eusouth1-lin-005','Dell','r710',4,2,"12/12/2020",5),
    ('eusouth1-phx-001','Cisco','VoicePhone',4,5,"12/12/2020",1),
    ('eusouth1-prn-001','HP','LaserJet 100',4,5,"12/12/2020",1),
    ('saeast1-dcc-001','Juniper','MX480',3,3,"12/12/2020",1),
    ('saeast1-dcd-001','Juniper','VCF 2500',3,4,"12/12/2020",1),
    ('saeast1-dcd-002','Juniper','VCF 2500',3,4,"12/12/2020",1),
    ('saeast1-dcd-003','Juniper','VCF 2500',3,4,"12/12/2020",1),
    ('saeast1-dcd-101','Juniper','VCF 1100',3,4,"12/12/2020",1),
    ('saeast1-dcd-102','Juniper','VCF 1100',3,4,"12/12/2020",1),
    ('saeast1-dcd-103','Juniper','VCF 1100',3,4,"12/12/2020",1),
    ('saeast1-dcd-104','Juniper','VCF 1100',3,4,"12/12/2020",1),
    ('saeast1-dcd-105','Juniper','VCF 1100',3,4,"12/12/2020",1),
    ('saeast1-dcd-106','Juniper','VCF 1100',3,4,"12/12/2020",1),
    ('saeast1-dcd-107','Juniper','VCF 1100',3,4,"12/12/2020",1),
    ('saeast1-dcd-108','Juniper','VCF 1100',3,4,"12/12/2020",1),
    ('saeast1-dcd-109','Juniper','VCF 1100',3,4,"12/12/2020",1),
    ('saeast1-tor-001','Cisco','Catalyst 9300',3,4,"12/12/2020",1),
    ('saeast1-tor-002','Cisco','Catalyst 9300',3,4,"12/12/2020",1),
    ('saeast1-tor-003','Cisco','Catalyst 9300',3,4,"12/12/2020",1),
    ('saeast1-tor-004','Cisco','Catalyst 9300',3,4,"12/12/2020",1),
    ('saeast1-tor-005','Cisco','Catalyst 9300',3,4,"12/12/2020",1),
    ('saeast1-tor-006','Cisco','Catalyst 9300',3,4,"12/12/2020",1),
    ('saeast1-tor-007','Cisco','Catalyst 9300',3,4,"12/12/2020",5),
    ('saeast1-tor-008','Cisco','Catalyst 9300',3,4,"12/12/2020",5),
    ('saeast1-tor-009','Cisco','Catalyst 9300',3,4,"12/12/2020",5),
    ('saeast1-tor-010','Cisco','Catalyst 9300',3,4,"12/12/2020",5),
    ('saeast1-boa-001','Cisco','Catalyst 3750',3,4,"12/12/2020",1),
    ('saeast1-boa-002','Cisco','Catalyst 3750',3,4,"12/12/2020",1),
    ('saeast1-boa-003','Cisco','Catalyst 3750',3,4,"12/12/2020",1),
    ('saeast1-boa-004','Cisco','Catalyst 3750',3,4,"12/12/2020",1),
    ('saeast1-boa-005','Cisco','Catalyst 3750',3,4,"12/12/2020",1),
    ('saeast1-boa-006','Cisco','Catalyst 3750',3,4,"12/12/2020",5),
    ('saeast1-boa-007','Cisco','Catalyst 3750',3,4,"12/12/2020",5),
    ('saeast1-boa-008','Cisco','Catalyst 3750',3,4,"12/12/2020",5),
    ('saeast1-boa-009','Cisco','Catalyst 3750',3,4,"12/12/2020",5),
    ('saeast1-boa-010','Cisco','Catalyst 3750',3,4,"12/12/2020",5),
    ('saeast1-boa-011','Cisco','Catalyst 3750',3,4,"12/12/2020",5),
    ('saeast1-boa-012','Cisco','Catalyst 3750',3,4,"12/12/2020",5),
    ('saeast1-win-001','Dell','r710',3,1,"12/12/2020",1),
    ('saeast1-win-002','Dell','r710',3,1,"12/12/2020",1),
    ('saeast1-win-003','Dell','r710',3,1,"12/12/2020",1),
    ('saeast1-win-004','Dell','r710',3,1,"12/12/2020",5),
    ('saeast1-win-005','Dell','r710',3,1,"12/12/2020",5),
    ('saeast1-lin-001','Dell','r710',3,2,"12/12/2020",1),
    ('saeast1-lin-002','Dell','r710',3,2,"12/12/2020",1),
    ('saeast1-lin-003','Dell','r710',3,2,"12/12/2020",1),
    ('saeast1-lin-004','Dell','r710',3,2,"12/12/2020",5),
    ('saeast1-lin-005','Dell','r710',3,2,"12/12/2020",5),
    ('saeast1-phx-001','Cisco','VoicePhone',3,5,"12/12/2020",1),
    ('saeast1-prn-001','HP','LaserJet 100',3,5,"12/12/2020",1)]

    ci_site1_topology_list=[('2022/06/01',2,4),
        ('2022/06/01',2,5),
        ('2022/06/01',2,6),
        ('2022/06/01',3,7),
        ('2022/06/01',3,8),
        ('2022/06/01',3,9),
        ('2022/06/01',4,2),
        ('2022/06/01',4,10),
        ('2022/06/01',4,11),
        ('2022/06/01',4,12),
        ('2022/06/01',5,2),
        ('2022/06/01',5,13),
        ('2022/06/01',5,14),
        ('2022/06/01',5,15),
        ('2022/06/01',6,2),
        ('2022/06/01',6,16),
        ('2022/06/01',6,17),
        ('2022/06/01',6,18),
        ('2022/06/01',7,3),
        ('2022/06/01',7,19),
        ('2022/06/01',7,20),
        ('2022/06/01',7,21),
        ('2022/06/01',8,3),
        ('2022/06/01',8,22),
        ('2022/06/01',8,23),
        ('2022/06/01',8,24),
        ('2022/06/01',9,3),
        ('2022/06/01',9,25),
        ('2022/06/01',9,26),
        ('2022/06/01',9,27),
        ('2022/06/01',10,4),
        ('2022/06/01',10,28),
        ('2022/06/01',10,29),
        ('2022/06/01',11,4),
        ('2022/06/01',11,30),
        ('2022/06/01',11,31),
        ('2022/06/01',12,4),
        ('2022/06/01',12,32),
        ('2022/06/01',12,33),
        ('2022/06/01',13,5),
        ('2022/06/01',13,34),
        ('2022/06/01',13,35),
        ('2022/06/01',14,5),
        ('2022/06/01',14,36),
        ('2022/06/01',14,37),
        ('2022/06/01',15,5),
        ('2022/06/01',15,38),
        ('2022/06/01',15,39),
        ('2022/06/01',16,6),
        ('2022/06/01',17,6),
        ('2022/06/01',18,6),
        ('2022/06/01',19,7),
        ('2022/06/01',19,40),
        ('2022/06/01',20,7),
        ('2022/06/01',20,41),
        ('2022/06/01',21,7),
        ('2022/06/01',21,42),
        ('2022/06/01',22,8),
        ('2022/06/01',22,43),
        ('2022/06/01',23,8),
        ('2022/06/01',23,44),
        ('2022/06/01',24,8),
        ('2022/06/01',24,45),
        ('2022/06/01',25,9),
        ('2022/06/01',25,46),
        ('2022/06/01',25,47),
        ('2022/06/01',26,9),
        ('2022/06/01',26,48),
        ('2022/06/01',27,9),
        ('2022/06/01',27,49),
        ('2022/06/01',28,10),
        ('2022/06/01',28,50),
        ('2022/06/01',28,51),
        ('2022/06/01',29,10),
        ('2022/06/01',29,54),
        ('2022/06/01',30,11),
        ('2022/06/01',31,11),
        ('2022/06/01',32,12),
        ('2022/06/01',33,12),
        ('2022/06/01',33,55),
        ('2022/06/01',34,13),
        ('2022/06/01',35,13),
        ('2022/06/01',36,14),
        ('2022/06/01',37,14),
        ('2022/06/01',37,56),
        ('2022/06/01',38,15),
        ('2022/06/01',39,15),
        ('2022/06/01',40,19),
        ('2022/06/01',40,52),
        ('2022/06/01',41,20),
        ('2022/06/01',41,53),
        ('2022/06/01',42,21),
        ('2022/06/01',43,22),
        ('2022/06/01',44,23),
        ('2022/06/01',44,57),
        ('2022/06/01',45,24),
        ('2022/06/01',46,25),
        ('2022/06/01',47,25),
        ('2022/06/01',47,58),
        ('2022/06/01',48,26),
        ('2022/06/01',49,27),
        ('2022/06/01',49,59)]

    insert_ci_topology_list(ci_site1_topology_list)   
   
   
   
   
   
   
    # insert one CI
    #insert_ci('us-core-01', 'Juniper', 'MX480')
    # insert multiple CI's
  #  insert_ci_list(ci_table_list)
    # insert_ci_location_list([
    #    # ('Mexico'),
    #    # ('London')
    #     ('Mexico', 23.6345, -102.5528),
    #     ('London', 51.5072, -0.1276),
    #     ('Houston', 29.7604, -95.3698),
    #     ('Toronto', 43.6532, -79.3832)
    # ])