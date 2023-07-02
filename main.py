import dearpygui.dearpygui as dpg
from window_ss import ImageProccess
import app
import time

loopStat = False

def start_callback(sender, app_data, user_data):

    # print("Start Clicked")
    # print(f"sender is: {sender}")
    # print(dpg.get_value(sender))
    # print(f"app_data is: {app_data}")
    # print(f"user_data is: {user_data}")
    loopStat = True
    
    while loopStat:
        # Yapılacak işlemler
        ImageProccess.pathToFileLength(ImageProccess)
        
        # Belirli bir süre bekleyin
        time.sleep(15)  # 5 saniye bekleyin
    return
def stop_callback():
    # app.setEmulatorSize("BlueStacks", 1280, 720)
    app.setEmulator()
    loopStat = False
    return
def print_value(sender):
    print(dpg.get_value(sender))
    return



dpg.create_context()
# dpg.show_documentation()
# dpg.show_style_editor()

with dpg.window(label="Window", width=600, height=600):
    dpg.add_text("Hello world")
    b0 = dpg.add_button(label="Start", width=150, height=40, callback=start_callback)
    b1 = dpg.add_button(label="Stop", width=150, height=40, callback=stop_callback)
    dpg.add_input_text(label="string", callback=print_value)
    # dpg.add_slider_float(label="float")
    with dpg.group():
        with dpg.table(header_row=True, row_background=True):

            # use add_table_column to add columns to the table,
            # table columns use child slot 0
            dpg.add_table_column()
            dpg.add_table_column()
            dpg.add_table_column()

            # add_table_next_column will jump to the next row
            # once it reaches the end of the columns
            # table next column use slot 1
            for i in range(0, 4):
                with dpg.table_row(height=40):
                    for j in range(0, 3):
                        dpg.add_text(f"{i}X{j}")


dpg.create_viewport(title='My Bot', width=600, height=600)
dpg.setup_dearpygui()
dpg.show_item_registry()
dpg.show_viewport()
dpg.start_dearpygui()

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    print("this will run every frame")
    dpg.render_dearpygui_frame()

dpg.destroy_context()