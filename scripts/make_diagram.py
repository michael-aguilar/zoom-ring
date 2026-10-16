from pathlib import Path
from html import escape
import json
p=Path(__file__).resolve().parents[1] / 'docs' / 'diagrams'
p.mkdir(parents=True, exist_ok=True)
W,H=1600,2370
s=[]
def text(x,y,t,size=25,color='#213046',weight=400,anchor='start'):
    s.append(f'<text x="{x}" y="{y}" font-family="Noto Sans, sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{escape(t)}</text>')
def rect(x,y,w,h,fill='#ffffff',stroke='#d1dae6',r=18):
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
def wire(points,color='#2668a5',width=4,dash=False):
    d='M '+' L '.join(f'{x},{y}' for x,y in points)
    s.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"'+(' stroke-dasharray="8 7"' if dash else '')+'/>')
def dot(x,y,c='#2668a5'):
    s.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{c}"/>')
def panel(y,h,num,title,sub):
    rect(48,y,1504,h)
    text(76,y+46,num,27,'#78889c',700)
    text(135,y+46,title,31,weight=700)
    text(76,y+83,sub,22,'#5b6c81')
def linkrow(y,left,right,color='#2668a5',x1=560,x2=1010):
    text(100,y+8,left,26)
    wire([(x1,y),(x2,y)],color)
    dot(x1,y,color);dot(x2,y,color)
    text(1040,y+8,right,26)
red='#bb3b38'; purple='#7550ae'; blue='#2668a5'; ground='#4c5b6b'
rect(0,0,W,H,'#f1f5fa','#f1f5fa',0)
text(56,67,'zoom controller / wiring v1',48,weight=700)
text(58,111,'XIAO RP2040 (standard) + Adafruit DRV8833 #3297 + N20 encoder motor #4639',24)
text(58,149,'Connection map, not physical pin placement. Repeated board names refer to the same board.',22,'#5b6c81')

panel(178,407,'01','power: one regulated 5 V USB source','Use a 5 V USB pack rated at least 1 A. Motor current branches before the XIAO.')
text(100,310,'USB +5 V',27,red,700)
wire([(290,302),(380,302)],red)
wire([(380,302),(430,279)],red);dot(380,302,red);dot(442,302,red)
text(361,346,'switch',21)
wire([(442,302),(610,302),(610,342),(1045,342)],red)
wire([(610,342),(610,412),(1045,412)],red);dot(610,342,red)
text(1070,350,'XIAO 5V / VBUS',27)
text(1070,420,'DRV8833 VM',27)
text(100,483,'USB ground',27,ground,700)
wire([(310,475),(650,475),(650,505),(1045,505)],ground)
wire([(650,475),(1045,475)],ground);dot(650,475,ground)
text(1070,483,'XIAO GND',27)
text(1070,532,'DRV8833 GND',27)
wire([(1045,505),(1045,524)],ground)
# Bulk capacitor bridges the driver's VM and GND rails.
wire([(875,412),(875,433)],red);dot(875,412,red)
wire([(851,433),(899,433)],ground,4)
wire([(851,447),(899,447)],ground,4)
wire([(875,447),(875,475)],ground);dot(875,475,ground)
text(910,439,'+',23,red,700)
text(689,384,'470 uF, >=10 V',22)
text(76,558,'C1 sits next to the driver: + to VM, - to GND. VM pad has no reverse-polarity protection.',22,'#5b6c81')

panel(608,396,'02','nunchuck: four connections','Cut-cable version. Identify the wires by function; clone colors are not standardized.')
text(100,731,'XIAO pin',25,weight=700);text(1040,731,'Nunchuck wire',25,weight=700)
linkrow(777,'3V3','VCC / 3.3 V',purple)
linkrow(826,'GND','GND',ground)
linkrow(875,'D4 / GPIO6','SDA (data)',blue)
linkrow(924,'D5 / GPIO7','SCL (clock)',blue)
text(100,971,'R1, R2: 4.7k each from SDA and SCL to 3V3. Use only one suitable pull-up set.',22,'#5b6c81')
# Small net-labelled pull-ups distinguish the two signal resistors.
# Pull-up details live in the explicitly labelled inset at the bottom.

panel(1027,340,'03','motor-driver control','3.3 V signals are valid for this driver. SLP is low/asleep by default.')
text(100,1150,'XIAO pin',25,weight=700);text(1040,1150,'DRV8833 pin',25,weight=700)
linkrow(1195,'D6 / GPIO0 (PWM)','AIN1',blue)
linkrow(1244,'D7 / GPIO1 (PWM)','AIN2',blue)
linkrow(1293,'D0 / GPIO26 (enable)','SLP',blue)
text(100,1339,'Firmware: keep SLP low at boot; enable only with valid input. Configure D2/D3 as INPUT_PULLUP.',22,'#5b6c81')

panel(1390,483,'04','motor + encoder: six connections','Wire colors below apply ONLY to Adafruit motor #4639. Other motors can differ.')
text(100,1513,'Source / board pin',25,weight=700);text(1040,1513,'Motor cable wire',25,weight=700)
linkrow(1558,'DRV8833 motor A output 1','red: motor terminal',red)
linkrow(1607,'DRV8833 motor A output 2','white: motor terminal',red)
linkrow(1656,'XIAO 3V3','black: encoder VCC',purple)
linkrow(1705,'common GND','blue: encoder GND',ground)
linkrow(1754,'XIAO D2 / GPIO28','yellow: encoder channel',blue)
linkrow(1803,'XIAO D3 / GPIO29','green: encoder channel',blue)
text(100,1848,'C2: 100 nF ceramic across red + white at the motor. Neither motor lead goes to GND.',22,'#5b6c81')

panel(1896,414,'05','small parts + build checks','All grounds are common. GPIO, nunchuck power and encoder power stay at 3.3 V.')
# explicit pull-up inset
text(100,2026,'3V3',24,purple,700)
wire([(184,2018),(240,2018)],purple)
rect(240,2007,95,22,'#f8fafc',purple,0)
wire([(335,2018),(430,2018)],blue)
text(255,2057,'4.7k',22);text(445,2026,'SDA',24,blue)
text(100,2111,'3V3',24,purple,700)
wire([(184,2103),(240,2103)],purple)
rect(240,2092,95,22,'#f8fafc',purple,0)
wire([(335,2103),(430,2103)],blue)
text(255,2142,'4.7k',22);text(445,2111,'SCL',24,blue)
text(610,2017,'1. Unplug external 5 V before PC USB programming.',23,weight=700)
text(610,2056,'2. Keep motor wires short and away from I2C wires.',23)
text(610,2095,'3. Stock driver current limit is 1 A, not lens protection.',23)
text(610,2134,'   Lower limit: replace its A-channel sense resistor.',23)
text(610,2173,'   I_limit = 0.2 / R_sense; do not add it in parallel.',23)
text(100,2228,'Start with motor/pulley detached. Firmware needs soft ramps, travel limits and stop-on-input-loss.',23)
text(100,2267,'Encoder feedback is relative: initialize a known position; belt slip is not sensed at the lens.',23)
text(58,2348,'Checked against Seeed + Adafruit documentation, 2026-10-15. Not bench-tested; lens torque/gearing not yet sized.',21,'#5b6c81')
svg='<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="2370" viewBox="0 0 1600 2370">'+''.join(s)+'</svg>'
(p/'zoom-wiring-v1.svg').write_text(svg)
(p/'zoom-wiring-v1.html').write_text('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Zoom controller wiring v1</title><style>body{margin:0;background:#f1f5fa;color:#213046;font:14px/1.4 system-ui}main{max-width:1200px;margin:24px auto;padding:0 12px}svg{width:100%;height:auto;display:block}</style><main>'+svg+'</main>')
# A compact machine-readable connection inventory supports the manual audit.
nets={
 '5V':['USB5V.switched','XIAO.5V','DRV8833.VM','C1.+'],
 'GND':['USB.GND','XIAO.GND','DRV8833.GND','Nunchuck.GND','Encoder.blue','C1.-'],
 '3V3':['XIAO.3V3','Nunchuck.VCC','Encoder.black','R1.1','R2.1'],
 'SDA':['XIAO.D4/GP6','Nunchuck.SDA','R1.2'],
 'SCL':['XIAO.D5/GP7','Nunchuck.SCL','R2.2'],
 'AIN1':['XIAO.D6/GP0','DRV8833.AIN1'],
 'AIN2':['XIAO.D7/GP1','DRV8833.AIN2'],
 'SLP':['XIAO.D0/GP26','DRV8833.SLP'],
 'ENC_YELLOW':['XIAO.D2/GP28','Encoder.yellow'],
 'ENC_GREEN':['XIAO.D3/GP29','Encoder.green'],
 'M1':['DRV8833.AOUT1','Motor.red','C2.1'],
 'M2':['DRV8833.AOUT2','Motor.white','C2.2']}
(p/'zoom-wiring-netlist.json').write_text(json.dumps(nets,indent=2))
print('wrote SVG, HTML and connection inventory')
