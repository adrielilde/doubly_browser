# Technical Challenge 2: Browser History Using a Doubly Linked List
# You are developing a web browser, and you need to implement a
# feature to manage the user’s browsing history, allowing them to go
#  back and forward through the visited pages.
# Authors: Adriel Ildefonso, email: aoir94@gmail.com
#          Alberto Maldonado, email: apimaldo@gmail.com
# Created: 07/31/2025

class SiteNode:
    def __init__(self, site):
        self.site = site
        self.next = None
        self.prev = None


class BrowserHistory:
    def __init__(self):
        self.head = None

    def visit_page(self, site):
        new_site = SiteNode(site)
        if self.head:
            self.head.next = None
            new_site.prev = self.head
            self.head.next = new_site
        self.head = new_site
        print(f"\n Current Page: {self.head.site} \n")

    def go_back(self):
        if self.head and self.head.prev:
            self.head = self.head.prev
            print(f"\n Back to: {self.head.site} \n")
        else:
            print("\n No previous page. \n")

    def go_forward(self):
        if self.head and self.head.next:
            self.head = self.head.next
            print(f"\n Forward to: {self.head.site} \n")
        else:
            print("\n No forward page. \n")


# Main Program

browser = BrowserHistory()

while True:
    print("===Terminal34 Browser===")
    print("Which action do you wish to perform?: ")
    print("1. Visit site/url")
    print("2. Exit browser")
    user_choice = input("Select option: ")

    if user_choice == "1":
        site = input("Please enter url/site to visit: ")
        browser.visit_page(site)
        while True:
            print("Browser Options: ")
            print("Press 1 to 'Visit new page'")
            print("Press 2 to 'Go Back'")
            print("Press 3 to 'Go Forward'")
            print("Press 4 to Exit Browser")
            navegation = input("Select option: ")

            if navegation == "1":
                site = input("Please enter url/site to visit: ")
                browser.visit_page(site)
            elif navegation == "2":
                browser.go_back()
            elif navegation == "3":
                browser.go_forward()
            elif navegation == "4":
                print("\n Browser closed \n")
                break
            else:
                print("\n Option not valid \n")
        break
    elif user_choice == "2":
        print("\n Browser closed \n")
        break
    else:
        print("\n Option not valid \n")
        