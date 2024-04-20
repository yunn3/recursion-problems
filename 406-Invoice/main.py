class Product:

    def __init__(self, title: str, price: float) -> None:
        self.title = title
        self.price = price


class InvoiceItem:

    def __init__(
        self,
        product: Product,
        quantity: int,
        next: "InvoiceItem" = None,
    ):
        self.product = product
        self.quantity = quantity
        self.next = next

    def getTotalPrice(self) -> float:
        totalprice = self.product.price * self.quantity
        return totalprice


class Invoice:
    def __init__(self, invoiceNumber: str, invoiceItemHead: "InvoiceItem") -> None:
        self.invoiceNumber = invoiceNumber
        self.invoiceItemHead = invoiceItemHead

    def amountDue(self, taxes: bool) -> float:
        taxrate = 1.1
        total_amount = 0
        invoice_item = self.invoiceItemHead
        while invoice_item is not None:
            total_amount += invoice_item.getTotalPrice()
            invoice_item = invoice_item.next

        if not taxes:
            return total_amount
        else:
            return total_amount * taxrate


product1 = Product("shampoo", 10)
product2 = Product("conditioner", 5)
product3 = Product("tooth brush", 3)

firstItem = InvoiceItem(product1, 7)
secondItem = InvoiceItem(product2, 9)
thirdItem = InvoiceItem(product3, 10)

firstItem.next = secondItem
secondItem.next = thirdItem

invoice = Invoice("UC1234567890", firstItem)


print(invoice.amountDue(False))  # --> 145
print(invoice.amountDue(True))  # --> 159.5
