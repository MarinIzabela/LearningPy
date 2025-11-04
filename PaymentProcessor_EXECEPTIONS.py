class PaymentProcessor:

    def process_payment(self):
        try:
            print("Processing payment........")
            payment_status = input("Enter Payment Status(success/fail): ").strip().lower()
            if payment_status == "fail":
                raise Exception("Payment Failed due to Network or Bank Issue.")
            else:
                print("Payment Status: " + payment_status)

        except Exception as error:
            print("Error: " + str(error))
            print("Saving cart items! Please try again later.")


payment_processor = PaymentProcessor()
payment_processor.process_payment()