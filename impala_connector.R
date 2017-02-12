# Connector using Cloudera ODBC Driver for connecting to an Impala service on a Hadoop database
library(RODBC)

impala_connect <- function() {
  require(RODBC)
  conn_str <- paste('driver={Cloudera ODBC Driver for Impala};host=<servername>;port=<port>;database=<databasename>;AuthMech=1;KrbServiceName=<servicename>;KrbRealm=<kerberosservicedomain>;KrbFQDN=<fullyqualifieddomainname>',sep='')
  myconn <<- odbcDriverConnect(conn_str)
  print("Connection Successful")
}
impala_connect()

query <- "<enter query here>"

data <- sqlQuery(myconn,
                 query,
                 rows_at_time=5000,
                 as.is=T)
