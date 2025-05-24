from flet import *
    
def main(page: Page):
   
    ##BG = '#041955'
    ##FGW = '97b4ff'
    ##FG = '#3450a1'
    ##PINK
    ## flet run 2.py
   

    def shrink(e):
        page_2.controls[0].width=100
        page_2.controls[0].scale=transform.Scale(0.5,alignment=alignment.center)
        page_2.controls[0].border_radius=border_radius.only(
            top_left=30,
            top_right=0,
            bottom_left=30,
            bottom_right=0,
        )
        page_2.update()

    def restore(e):
        page_2.controls[0].width=340
        page_2.controls[0].scale=transform.Scale(1,alignment=alignment.center)
        page_2.update()
    
    create_task_view = Container(   
        content=Container(on_click=lambda _: page.go("/"),
                          content=Icon(icons.CLOSE,color='white'),)
    )
    
    tasks = Column(
        height=360,
        scroll='auto',
        controls=(
        
        )    
    )

    for i in range(10):
        tasks.controls.append(
            Container(height=50,width=300,
                      bgcolor='#041955',
                      border_radius=25,
                      padding=padding.only(left=15,top=15,bottom=15),
                      content=Checkbox(fill_color='#041955',
                                       check_color='white',
                                       label='hello Ezoo how do you do',
                                       )
                                                           
                        
                      ),
            )

    categories_card =Row(
        scroll='auto'
    )

    categories =['Business','Family','Frinde']
    for i ,category in enumerate(categories):
        categories_card.controls.append(
            Container(
              bgcolor='#041955',
              height=90,
              border_radius=20,
              width=140,
              padding=20,
              content=Column(
                controls=[
                    Text('40 Tasks',color='white',),
                    Text('category',color='white',),
                  
                    Container(
                        width=130,
                        height=5,
                        bgcolor='white12',
                        padding=padding.only(right=i*25),
                        content=Container(
                            bgcolor='pink',
                        )
                    )
                ]
              )
            )
        )

########################################################################################################################
########################################################################################################################

    first_page_contents = Container(               ##  الصفحه الاساسيه عند الدخول  ##
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                    controls=[
                        Container(
                            content=Icon(icons.MENU,color='white'),
                            on_click=lambda e:shrink(e)
                       ),
                       Row(
                            controls=[
                                Icon(icons.SEARCH,color='white'),
                                Icon(icons.NAVIGATION,color='white')
                            ]
                       ),
                   ],
                ),

                Text(
                    value ='what\'s up, Eezoo', 
                    size=30,color='white'                  
                ),
                Text(
                    value ='CATEGORIES',color='white'                   
                ),
                Container(
                    padding=padding.only(top=10,bottom=10),
                    content=categories_card
                ),
                Container(height=20),
                Text('TODAY\'S TASKS'),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(
                            bottom=5,right=10,
                            icon=icons.ADD,bgcolor='white34',
                            on_click=lambda _: page.go('/create_task')
                        )
                    ]
                )
            ],
        ),
    )

########################################################################################################################
########################################################################################################################


    page_1 = Container(                             ##   الصفحه الاولى __الاسم و الاضافات ##
                width=340,
                height=720,
                bgcolor='#041955',
                border_radius=25,
                padding=padding.only(
                    top=50,left=40,right=150),
        content=Column(
            controls=[
                Row(
                    controls=[
                        Container(
                    height=40,width=40,
                    border_radius=20,
                    on_click=lambda e: restore(e),
                    border=border.all(color='white',width=2),
                    content=Icon(icons.ARROW_BACK,color='white'),
                )
                    ]
                ),
                Container(height=20),
                ##circle,
                Text('Eezoo\nZee',size=30,weight='bold'),
                Container(height=3),
                Row(controls=[
                    Icon(icons.FAVORITE_BORDER_SHARP) ,
                    Text('FAVORITE',weight=FontWeight.W_300,size=18,color='white')]
                    ),
                Container(height=3),
                Row(controls=[
                    Icon(icons.CARD_GIFTCARD_OUTLINED) ,
                    Text('CARD',weight=FontWeight.W_300,size=18,color='white')]
                    ),
                Container(height=3),
                Row(controls=[
                    Icon(icons.CALCULATE_OUTLINED) ,
                    Text('CALCULATE',weight=FontWeight.W_300,size=18,color='white')]
                    ),
                Container(height=3),   
                Row(controls=[
                    Icon(icons.SHOP_TWO_OUTLINED) ,
                    Text('SHOP',weight=FontWeight.W_300,size=18,color='white')]
                    ),
                    Row(controls=[
                    Icon(icons.LINE_AXIS_ROUNDED,size=160),
                    ]
                    ),
                    Text('Good',font_family='poppins'),
                    Text('Consistency',size=20,color='white')
                
            ]
        ),
    )

########################################################################################################################
########################################################################################################################

    page_2 = Row(alignment='end',        ##  الصفحه الصفحه الاولى ولكن عند السحب تتحول الى صغيره  ##
        controls=[
            Container(
                width=340,
                height=720,
                bgcolor='#3450a1',
                animate=animation.Animation(500,AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(300,curve='decelerate'),
                border_radius=25,
                padding=padding.only(
                    top=50,left=20,right=20,bottom=5
                ),
                content=Column(
                    controls=[
                        first_page_contents
                    ]
                ) 
            )
        ]
    )

########################################################################################################################
########################################################################################################################

    container = Container(              ##  الصفحه الرئيسه الاساسيه ##
        width=340,
        height=720,
        bgcolor='#041955',
        border_radius=25,
        content=Stack(
          controls=[
            page_1,
            page_2,
          ]
          
        )
    )

    
    pages ={                                      ##  الصفحه السودا الثالثه  ##
        "/":View(
            "/",
            [
                container
            ],
        ),
        "/create_task" : View(
            "/create_task",
            [
                create_task_view
            ]
        )
    }

    def route_Change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )
    
    page.add(container)

    page.on_route_change = route_Change 
    page.go(page.route)

    page.update()
app(target=main)






