from asyncio.windows_events import NULL
import psycopg2
from psycopg2.extras import RealDictCursor
from config import config
from neo4j import GraphDatabase
import numpy as np
import json, codecs
from py2neo import Graph
from Neo4jConnection import Neo4jConnection


def select_all_ci():
    """read the CI table  """
    sql = 'SELECT  t."ciID", t."neighborID", t."interface", c."ciName", d."ciName" as neighborName, c."ciBrand", c."ciModel", t."timestamp" FROM "TPFinal"."CI_Topology" t INNER JOIN "TPFinal"."CI_Table" c ON t."ciID" = c."idCi" INNER JOIN "TPFinal"."CI_Table" d ON t."neighborID" = d."idCi"'
    conn = None
    result= NULL
    try:
        # read database configuration
        params = config("","POSTGRES")
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        #result= cur.fetchone()
        result= cur.fetchmany(3)
        #result= cur.fetchall()
        result=np.array(result)
        result= result.astype('str')
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return result

def select_from_db(sql):
    """read the CI table  """
    conn = None
    result= NULL
    try:
        # read database configuration
        params = config("","POSTGRES")
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return result

def upload_neo4j(ci_list):
    params = config("","NEO4J")
    query_string= """CALL apoc.load.json("file://ci.json") yield value
                        MERGE (ci:CI {ciID: value.ciID})
                        SET ci.Name = value.ciName
                        SET ci.ciBrand = value.ciBrand
                        SET ci.ciModel = value.Model
                        SET ci.Interface = value.Interface
                        WITH ci, value
                        UNWIND value.neighbors as neighbor
                        MERGE (n:CI {ciID: neighbor})
                        MERGE (n)-[:Connected_to]->(ci);"""
    conn=Neo4jConnection(**params)
    query_params=ci_list
    conn.query(query_string, query_params , db='neo4j')


if __name__ == '__main__':
    #invoke sql select * and remove trailing spaces

    
    sql1="""SELECT h."ciID", 
					regexp_replace(h."ciName", '\s+$', '') as "ciName", 
					regexp_replace(h."ciBrand", '\s+$', '') as "ciBrand", 
					regexp_replace(h."ciModel", '\s+$', '') as "ciModel", 
					h."neighbors" FROM (
			SELECT t."ciID",c."ciName",c."ciBrand",c."ciModel", json_agg(t."neighborID") as neighbors 
			FROM "TPFinal"."CI_Topology" t
			INNER JOIN "TPFinal"."CI_Table" c ON t."ciID" = c."idCi"
			GROUP BY t."ciID", c."ciName",c."ciBrand", c."ciModel"
			ORDER BY t."ciID") h
    
    """
    

    
    ci_list = select_from_db(sql1)
    # print (type(ci_list))
    ci_json = json.dumps(ci_list)

    upload_neo4j(ci_json)

    # ci_json = json.dumps(ci_list,indent=2)
    # # for ci in  ci_json[]:
    # #     print(ci)
    #     # ci["neighbor_list"] = ci["neighbors"].split(',')
    # #print(ci_json)
    # with open('C:\\Users\\marti\\OneDrive\\Documents\\CEIOT\\AAD\\TP_Final\\ci.json','w', encoding='utf-8') as f:
    #     json.dump(ci_list,f,ensure_ascii=False, indent=4)
    # f.close()  


  #Neo4j data upload
#     graph = Graph("bolt://localhost:7687", user="neo4j", password="password")
#     result = graph.run(
#     """WITH $ci_json as data
#     UNWIND data as ci
#     MATCH (c:CI {id: id}) RETURN c.name""", 
#     json=json
# )
# data_frame_result = result.to_data_frame()
# print(data_frame_result)

    # transaction_execution_commands = []
    # query_str = np.array(['create (t:Topology {ciID:', 'NeighborID:','Interface:','ciName:','NeighborName:','ciBrand:','ciModel:','TimeStamp:'])
    # transaction_execution_commands = list(np.char.add(query_str, ci_list))
    # test = np.append(transaction_execution_commands,")")
    # print(test)
    #execute_transactions(transaction_execution_commands)




