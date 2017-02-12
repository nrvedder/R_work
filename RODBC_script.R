# Connector for MS SQL Server
library(RODBC)

query <- "<enter query here>"

sql.query <- function(server,database,query) {
    library(RODBC)
    myconn <<- odbcDriverConnect(paste('driver={SQL Server};server=',server,';database=',database,';trusted_connection=true',sep = ""))
    data <- sqlQuery(myconn,query)
    odbcCloseAll()
    return(data)
  }

data <- sql.query("<servername>","<databasename>",query)
