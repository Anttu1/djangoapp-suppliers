from django.db import models

class Supplier(models.Model):
    companyname = models.CharField(max_length= 50, default="firma")
    contactname = models.CharField(max_length= 50, default="firma")
    address = models.CharField(max_length= 100, default="firma")
    phone = models.CharField(max_length= 20, default="firma")
    email = models.CharField(max_length= 50, default="firma")
    country = models.CharField(max_length= 50, default="firma")

    # ao:n voi tehdä jos haluaa että admin sivu toimii myöhemmässä vaiheessa paremmin,
    # mutta se ei ole välttämätöntä alussa
    def __str__(self):
        return f"{self.companyname} from {self.country}"

class Product(models.Model):
    productname = models.CharField(max_length= 50, default="laku")
    packagesize = models.CharField(max_length= 50, default=3)
    unitprice = models.DecimalField(max_digits= 8, decimal_places=2, default=1.00)
    unitsinstock = models.IntegerField(default=3)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    # ao: n voi tehdä jos haluaa että admin sivu toimii myöhemmässä vaiheessa hienommin,  mutta ei ole välttämätöntä alussa   
    def __str__(self):
        return f"{self.productname} produced by {self.supplier.companyname}"
    
class Customer(models.Model):
    customername = models.CharField(max_length= 50, default="asiakas")
    address = models.CharField(max_length= 100, default="asiakas")
    phone = models.CharField(max_length= 20, default="asiakas")
    email = models.CharField(max_length= 50, default="asiakas")
    country = models.CharField(max_length= 50, default="asiakas")

class Car(models.Model):
    brand = models.CharField(max_length= 30, default="toyota")
    model = models.CharField(max_length= 30, default="yaris")
    licenseplate = models.CharField(max_length= 50, default=3)
    owner = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.licenseplate} owned by {self.supplier.companyname}"

