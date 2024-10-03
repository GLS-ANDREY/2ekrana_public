import time,view,controller,model,view2,controller2

while True:
    time.sleep(1/100)
    if model.ekran == 0:
        view.risovanie()
        controller.allsobitiya()
    if model.ekran == 1:
        view2.risovanie2()
        controller2.allsobitiya2()

