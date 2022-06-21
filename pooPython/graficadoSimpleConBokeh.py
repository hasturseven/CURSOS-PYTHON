from bokeh.plotting import figure,output_file, show


output_file('graficado_simple.html')
fig=figure()

total_valores_graficar=int(input('cuantos valores quieres graficar'))

x_valores=list(range(total_valores_graficar))
y_valores=[]

for x in x_valores:
  val=int(input(f'valor y para {x}'))
  y_valores.append(val)

fig.line(x_valores,y_valores,line_width=5)

show(fig)