from flet import *

def main(page: Page):
    page.title = " My Vat app"
    page.window.height = 740
    page.window.width = 390
    page.window.top = 10
    page.window.left = 960
    page.theme_mode = ThemeMode.LIGHT

    def route_change(route):
        page.views.clear()
        page.views.append(
           View("/",
                [
                 AppBar(
                    title= Text("My Vat app"),
                    color="white",
                    elevation=2,
                    bgcolor = colors.PINK,
                ),
                 Text('Hello Vat'),
                 ElevatedButton("login" , on_click=lambda _: page.go("/login")),
                 ElevatedButton("New User" , on_click=lambda _: page.go("/signup"))  
                ]
                )
        )
        if page.route == "/login":
            page.views.append(
            View("/login",
                [
                AppBar(
                    title= Text("My Login Page"),
                    color="white",
                    elevation=2,
                    bgcolor = colors.GREEN_300,
                ),
                 Text('Login page'),
                 ElevatedButton("New User" , on_click=lambda _: page.go("/signup"))     
                ]
                ))
        if page.route == "/signup":
            page.views.append(
            View("/signup",
                [
                 AppBar(
                    title= Text("Sign Up Page"),
                    color="white",
                    elevation=2,
                    bgcolor = colors.PURPLE,
                ),
                 Text('signup page'),
                 ElevatedButton("I have account" , on_click=lambda _: page.go("/login"))     
                ]
                ))
        page.update()
    def page_go(view):
        page.views.pop()
        back_page = page.views[-1]
        page.go(back_page.route)

    page.on_route_change = route_change
    page.on_view_pop = page_go
    page.go(page.route)

app(main)
