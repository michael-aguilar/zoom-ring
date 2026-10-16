from pathlib import Path
from html import escape
import json
import xml.etree.ElementTree as ET
p=Path(__file__).resolve().parents[1] / 'docs' / 'diagrams'
W,H=2160,1440
bg='#f7f9fc'; ink='#182b43'; muted='#53657c'
red='#ba3d35'; purple='#8150b1'; signal='#2466a9'; feedback='#117f83'; ground='#627184'
wires=[]; nodes=[]; labels=[]; ports=[]
def txt(x,y,t,size=25,c=ink,weight=400,anchor='start'):
    labels.append(f'<text x="{x}" y="{y}" fill="{c}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" font-family="Noto Sans">{escape(t)}</text>')
def path(d,c=signal,w=4):
    wires.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')
def line(points,c=signal,w=4):
    path('M '+' L '.join(f'{x},{y}' for x,y in points),c,w)
def dot(x,y,c):
    ports.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{c}"/>')
def box(x,y,w,h,fill):
    nodes.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="#b3c2d3" stroke-width="2"/>')
def pin(x,y,c):
    ports.append(f'<circle cx="{x}" cy="{y}" r="5" fill="{bg}" stroke="{c}" stroke-width="3"/>')
def resistor(x,y):
    wires.append(f'<rect x="{x-10}" y="{y}" width="20" height="52" fill="{bg}" stroke="{purple}" stroke-width="3"/>')
# Switched 5 V branches before the controller. Ground is one continuous bus.
line([(440,230),(540,230)],red)
line([(540,230),(599,203)],red)
line([(610,230),(1830,230)],red)
pin(540,230,red);pin(610,230,red)
line([(1050,230),(1050,440)],red);dot(1050,230,red)
line([(1620,230),(1620,440)],red);dot(1620,230,red)
line([(100,315),(50,315),(50,1240),(2070,1240),(2070,294)],ground)
line([(100,740),(50,740)],ground);dot(50,740,ground)
line([(870,1100),(870,1240)],ground);dot(870,1240,ground)
# Bulk capacitor close to the driver's power entry.
line([(1830,230),(1830,278)],red)
line([(1804,278),(1856,278)],ground)
line([(1804,294),(1856,294)],ground)
line([(1830,294),(1830,340),(2070,340)],ground);dot(2070,340,ground)
txt(1866,274,'+',25,red,700)
txt(1665,293,'470 µF',25);txt(1665,326,'10 V min',23,muted)
# Logic rail, with explicit wire bridges at the two unrelated 5 V drops.
path('M 240,500 L 240,370 L 1038,370 Q 1050,346 1062,370 L 1608,370 Q 1620,346 1632,370 L 1980,370 L 1980,920 L 1880,920',purple)
line([(870,370),(870,440)],purple);dot(870,370,purple)
# I2C pair, optional pull-ups visibly connected to the same 3.3 V rail.
line([(440,600),(800,600)],signal)
line([(440,660),(800,660)],signal)
line([(540,370),(540,438)],purple);resistor(540,438);line([(540,490),(540,600)],purple)
line([(650,370),(650,438)],purple);resistor(650,438)
path('M 650,490 L 650,588 Q 674,600 650,612 L 650,660',purple)
dot(540,370,purple);dot(650,370,purple);dot(540,600,signal);dot(650,660,signal)
# Controller to driver.
for y in (540,600,660): line([(1180,y),(1440,y)],signal)
# Bridge ground past the encoder supply without making a junction.
path('M 1880,660 L 1968,660 Q 1980,636 1992,660 L 2070,660',ground);dot(2070,660,ground)
# Motor bridge outputs and 100 nF brush-noise capacitor.
line([(1700,740),(1700,840)],red)
line([(1780,740),(1780,840)],red)
line([(1700,785),(1732,785)],red)
line([(1748,785),(1780,785)],red)
line([(1732,768),(1732,802)],ground)
line([(1748,768),(1748,802)],ground)
dot(1700,785,red);dot(1780,785,red)
line([(1880,1110),(2070,1110)],ground);dot(2070,1110,ground)
# Closed-loop feedback returns directly to the controller.
for y in (1000,1060): line([(1180,y),(1440,y)],feedback)
# Component blocks. Each physical component appears once.
box(100,180,340,160,'#ffffff')
box(100,500,340,300,'#eef5fd')
box(800,440,380,660,'#eef1fc')
box(1440,440,440,300,'#eef1fc')
box(1440,840,440,310,'#eaf5f2')
# Page title and rail labels.
txt(100,78,'zoom controller / one connected wiring diagram',43,ink,700)
txt(100,122,'standard XIAO RP2040 + Adafruit DRV8833 #3297 + Adafruit N20 encoder motor #4639',25,muted)
txt(1110,207,'switched +5 V',25,red,700)
txt(1120,345,'3.3 V logic power',25,purple,700)
txt(580,184,'power switch',23,muted,anchor='middle')
txt(124,215,'USB battery',28,ink,700)
txt(124,257,'5 V, 1 A min',26)
txt(416,222,'+5 V',22,red,anchor='end');txt(124,323,'GND',23,ground)
# Nunchuck.
txt(124,562,'wired nunchuck',28,ink,700)
txt(240,530,'VCC',23,purple,anchor='middle')
txt(416,608,'SDA',24,signal,anchor='end')
txt(416,668,'SCL',24,signal,anchor='end')
txt(124,748,'GND',24,ground)
txt(512,465,'4.7k',23,purple,anchor='end');txt(676,465,'4.7k',23,purple)
txt(478,722,'I²C pull-ups',24,ink,700)
txt(478,754,'omit if already fitted',22,muted)
# XIAO physical board shown once; functional pin placement only.
txt(870,475,'3V3',24,purple,anchor='middle');txt(1050,475,'5V',24,red,anchor='middle')
txt(824,608,'D4 / GP6',24,signal);txt(824,668,'D5 / GP7',24,signal)
for y,t in [(540,'D6 / GP0'),(600,'D7 / GP1'),(660,'D0 / GP26')]: txt(1156,y+8,t,24,signal,anchor='end')
txt(990,776,'XIAO',46,ink,700,anchor='middle')
txt(990,823,'RP2040',35,ink,700,anchor='middle')
txt(990,866,'controller',25,muted,anchor='middle')
txt(1156,1008,'D2 / GP28',24,feedback,anchor='end')
txt(1156,1068,'D3 / GP29',24,feedback,anchor='end')
txt(870,1078,'GND',24,ground,anchor='middle')
# Driver.
txt(1464,483,'DRV8833',31,ink,700);txt(1464,515,'Adafruit #3297',22,muted)
txt(1620,428,'VM',23,red,anchor='middle')
for y,t in [(540,'AIN1'),(600,'AIN2'),(660,'SLP')]: txt(1464,y+8,t,25,signal)
txt(1856,668,'GND',24,ground,anchor='end')
txt(1700,716,'AOUT1',20,red,anchor='middle');txt(1780,716,'AOUT2',20,red,anchor='middle')
for y,t in [(540,'PWM / direction'),(600,'PWM / direction'),(660,'enable')]: txt(1310,y-13,t,21,signal,anchor='middle')
# Motor, including its encoder in the same component box.
txt(1464,888,'N20 + encoder',30,ink,700);txt(1464,925,'Adafruit #4639',22,muted)
txt(1687,827,'red',21,red,anchor='end');txt(1793,827,'white',21,red)
txt(1667,791,'100 nF',24,ink,anchor='end')
txt(1856,963,'black: encoder VCC',24,purple,anchor='end')
# VCC label needs a short internal leader to the right-side power pin.
nodes.append(f'<path d="M 1880,920 L 1847,920 L 1847,937" fill="none" stroke="{purple}" stroke-width="2"/>')
txt(1464,1008,'yellow: encoder A',24,feedback)
txt(1464,1068,'green: encoder B',24,feedback)
txt(1856,1118,'blue: GND',24,ground,anchor='end')
txt(1310,986,'encoder A',22,feedback,anchor='middle')
txt(1310,1046,'encoder B',22,feedback,anchor='middle')
# Context in open space, not separate wiring panels.
txt(100,934,'closed-loop feedback',28,ink,700)
txt(100,974,'D2 / D3: enable input pull-ups in firmware',24,muted)
txt(100,1016,'SLP: keep low at boot; high enables the driver',24,muted)
txt(100,1058,'Nunchuck cable colors vary: identify by function',24,muted)
txt(1110,1226,'common ground',26,ground,700)
# Connector endpoints.
for x,y,c in [(440,230,red),(100,315,ground),(100,740,ground),(240,500,purple),(440,600,signal),(440,660,signal),(800,600,signal),(800,660,signal),(870,440,purple),(1050,440,red),(870,1100,ground),(1620,440,red),(1880,660,ground),(1700,740,red),(1780,740,red),(1700,840,red),(1780,840,red),(1880,920,purple),(1880,1110,ground)]:pin(x,y,c)
for y in (540,600,660):pin(1180,y,signal);pin(1440,y,signal)
for y in (1000,1060):pin(1180,y,feedback);pin(1440,y,feedback)
txt(100,1300,'Pin connections, not physical pin placement. Wire colors apply only to motor #4639. Dots join wires; bridges do not.',24,muted)
txt(100,1340,'Unplug external 5 V before PC USB programming. Lower/tune the driver current limit before connecting the lens.',24,ink,700)
txt(100,1380,'Documentation-checked circuit, not bench-tested. Motor current branches before the XIAO; GPIO stays at 3.3 V.',24,muted)
svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="{bg}"/>'+''.join(wires+nodes+ports+labels)+'</svg>'
ET.fromstring(svg)
(p/'zoom-wiring-unified.svg').write_text(svg)
(p/'zoom-wiring-unified.html').write_text('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Zoom controller wiring</title><style>body{margin:0;background:#f7f9fc;font-family:system-ui}main{margin:auto;max-width:2160px}svg{width:100%;height:auto;display:block}</style><main>'+svg+'</main>')
print('wrote unified SVG and HTML; XML valid')
