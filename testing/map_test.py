from tkinter import *
import tkintermapview

app = Tk()
app.title("test")
app.geometry("900x700")

my_label = LabelFrame(app)
my_label.pack(pady=20)

map = tkintermapview.TkinterMapView(my_label,width=800,height=600,corner_radius=0)
map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
map.set_position(23.97565, 120.9738819)
map.set_zoom(7.4)

map.pack()

polygon = map.set_polygon([(25.945523174000073,119.96445191400005),
                        (25.94553105400007,119.96447095600001),
                        (25.94554007700009,119.9644900080001),
                        (25.945553652000058,119.964512893),
                        (25.945561601000065,119.96452181400002),
                        (25.94557295900006,119.96453392600006),
                        (25.94561688300007,119.96455136500003),
                        (25.945630575000052,119.96455653700002),
                        (25.945648279000068,119.96456047700008),
                        (25.94566547900007,119.96455429000002),
                        (25.945729997000058,119.96448523000004),
                        (25.94574441800006,119.964467001),
                        (25.945745612000053,119.96445941900004),
                        (25.945742323000047,119.96443788400006),
                        (25.94573285200005,119.96439985000006),
                        (25.94565553700005,119.96424359800005),
                        (25.94565388500007,119.96423409600004),
                        (25.94564316000009,119.96421249900004),
                        (25.94563240800005,119.96419533100004),
                        (25.94558820800006,119.96415925000008),
                        (25.94551840400004,119.9641374680001),
                        (25.945500055000082,119.96414427800005),
                        (25.94549587100005,119.96417144500003),
                        (25.945495744000084,119.9641904230001),
                        (25.945488368000042,119.96426754100003),
                        (25.945523174000073,119.96445191400005)])

app.mainloop()