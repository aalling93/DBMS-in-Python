    def addCustomer(self, customerId, customerName):
        """Inserts a customer into the database"""
        cursor = self.cnx.cursor()
        query = "INSERT INTO Customer (CustomerId, CustomerName) VALUES ('E13', 'E')" #% (customerId,customerName)
        cursor.execute(query) 
        cursor.close()
        self.cnx.commit()
        
        
        return
        
    def deleteCustomer(self, customerId):
        """Deletes a customer from the database"""
        cursor = self.cnx.cursor()
        query = "DELETE FROM Customer (CustomerId, CustomerName) WHERE CustomerId=%s"
        cursor.execute(query,customerId)
        cursor.close()
        self.cnx.commit()
        
        
        # TODO: Execute statement. Make sure to commit
        return   
    
    def updateCustomer(self, customerId, customerName):
        """Updates a customer in the database"""
        cursor = self.cnx.cursor()
        query = "UPDATE Customer SET CustomerId=%s, CustomerName=%s WHERE CustomerId=%s" %(customerId, customerName, customerId)
        cursor.execute(query)
        cursor.close()
        self.cnx.commit()
        # TODO: Execute statement. Make sure to commit
        return 
