import pandas as pd
import matplotlib
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF


df = pd.DataFrame()
df['Mes'] = ["Q1", "Q2", "Q3", "Q4","Q5", "Q6", "Q7", "Q8", "Q9"]
df['MWh'] = [1050, 1100, 1150, 900, 930, 980, 910, 940, 890]

title("Consumo Mensuales")
xlabel('Mes')
ylabel('MWh')

# SE DEFINE LAS VARIABLES A USAR EN EL PLOT
c = [1,2,3,4,5,6,7,8,9]
m = [x - 0 for x in c]

xticks(c, df['Mes'])
# DEFINE EL ESTILO DE LAS BARRAS 
bar(m, df['MWh'], width=0.5, color="#2B6538", label="MWh")

legend()
axis([0, 10, 0, 8])
savefig('barchart.png')

pdf = FPDF()
pdf.add_page()
pdf.set_xy(0, 0)
pdf.set_font('arial', 'B', 12)
pdf.cell(60)
pdf.cell(75, 10, "Estado de Cuenta Suministro Calificado"+" "*60+"BEETMANN", 0, 2, 'C')
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(-40)
pdf.cell(50, 10, 'Nombre y Dirección', 0, 0, 'C')
pdf.cell(50, 10, 'Periodo y Total a Pagar', 0, 0, 'C')
pdf.cell(-90)
pdf.set_font('arial', '', 10)

# AQUI SE COLOCA LA GRAFICA X,Y
for i in range(0, len(df)):
    pdf.cell(50, 10, '%s' % (df['Mes'].iloc[i]), 1, 0, 'C')
    pdf.cell(40, 10, '%s' % (str(df.MWh.iloc[i])), 1, 0, 'C')
    pdf.cell(-90)
pdf.cell(90, 10, " ", 0, 2, 'C')
pdf.cell(-30)
pdf.image('barchart.png', x = None, y = None, w = 0, h = 0, type = '', link = '')

pdf.output('test.pdf', 'F')
