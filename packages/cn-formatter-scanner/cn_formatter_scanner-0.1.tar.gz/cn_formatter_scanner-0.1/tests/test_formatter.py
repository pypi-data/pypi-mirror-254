import pytest
from formatter.formatter import CNFormatter

# Basic tests for each calculator function

def test_addition():
    ft = CNFormatter()
    assert ft.title_formatter('Hello! Hello  New York United States','New York','New York', 'United States') == 'hello'

def test_addition2():
    ft = CNFormatter()
    assert ft.title_formatter('Paris 14th Montparnasse ID 301','Paris','Ile-De-France', 'France') == '14thmontparnasseid301'

def test_addition3():
    ft = CNFormatter()
    assert ft.title_formatter('Apartment WS Hôtel de Ville Pompidou','Paris','Ile-De-France', 'France') == 'apartmentwsdevillepompidou'

def test_addition4():
    ft = CNFormatter()
    assert ft.title_formatter('Céleste Hôtel à Paris','Paris','Ile-De-France', 'France') == 'celeste'

def test_addition5():
    ft = CNFormatter()
    assert ft.title_formatter('Central // 3BR Penthouse // Terrace // Duplex','London','England', 'United Kingdom') == 'central3brpenthouseterraceduplex'

def test_addition6():
    ft = CNFormatter()
    assert ft.title_formatter('100 Sunset Hotel - CHSE Certified','Badung','Bali', 'Indonesia') == '100sunset'

def test_addition7():
    ft = CNFormatter()
    assert ft.title_formatter('_________Long term vacation? Relax,Work, Play, Repeat','Tsilivi','Decentralized Administration Of Peloponnese', 'Western Greece And The Ionian') == 'longtermvacationrelaxworkplayrepeat'

def test_addition8():
    ft = CNFormatter()
    assert ft.title_formatter('Jean&apos;s Beach Retreat','Tybee Island','Georgia', 'United States') == 'jeanapossbeachretreat'
    
def test_addition9():
    ft = CNFormatter()
    assert ft.title_formatter('At Hotel New York','New York','New York', 'United States') == 'athotel'

def test_addition10():
    ft = CNFormatter()
    assert ft.title_formatter('The Taj Hotel Dehli','Dehli','Mahrashtra', 'Inida') == 'taj'

def test_addition11():
    ft = CNFormatter()
    assert ft.title_formatter('Holiday Inn Express & Suites Gulf Shores, an IHG Hotel','Gulf Shores','Alabama', 'United States') == 'holidayinnexpress'

def test_addition11():
    ft = CNFormatter()
    assert ft.title_formatter('The Bostancı Hotel','Istanbul','Istanbul', 'Turkey') == 'bostanci'

def test_addition12():
    ft = CNFormatter()
    assert ft.title_formatter("🌅 1̶0̶0̶ 𝓢𝓾𝓷𝓼𝓮𝓽 𝓗𝓸𝓽𝓮𝓵 - 𝒞ℋ𝒮ℰ 𝓒𝑒𝓇𝓉𝓲𝒻𝓲𝑒𝒹 🌅",'London','England', 'United Kingdom') == '100'

def test_addition13():
    ft = CNFormatter()
    title = ft.title_formatter("The 100 Sunset Hotel - A 𝕮𝕳𝕾𝕰 ℂ𝕖𝕣𝕥𝕚𝕗𝕚𝕖𝕕",'London','England', 'United Kingdom')
    assert  title == '100sunset'
    assert ft.get_property_key(title, 'London','England', 'United Kingdom') == '208379f3bac1b0ac8548e12cf1097bbe'

def test_addition14():
    ft = CNFormatter()
    assert ft.title_formatter("𝟙𝟘𝟘 𝕊𝕦𝕟𝕤𝕖𝕥 ℍ𝕠𝕥𝕖𝕝 - ℂℍ𝕊𝔼 ℂ𝕖𝕣𝕥𝕚𝕗𝕚𝕖𝕕",'London','England', 'United Kingdom') == ''

def test_addition15():
    ft = CNFormatter()
    title = ft.title_formatter("100 Sünšèt Hôtël - ĆHŚÈ Ćërtífíëd",'London','England', 'United Kingdom')
    assert  title == '100sunset'
    assert ft.get_property_key(title,'London','England', 'United Kingdom') == '208379f3bac1b0ac8548e12cf1097bbe'

def test_addition16():
    ft = CNFormatter()
    title = ft.title_formatter("The 100 Sůnşệţ Hòtệl - ĊĦŜẸ Ċệrťíƒíệd",'London','England', 'United Kingdom')
    assert  title == '100sunset'
    assert ft.get_property_key(title, 'London','England', 'United Kingdom') == '208379f3bac1b0ac8548e12cf1097bbe'

def test_addition17():
    ft = CNFormatter()
    title = ft.title_formatter("The 100 $un$et Hotel - CHSE Certified",'London','England', 'United Kingdom')
    assert  title == '100sunset'
    assert ft.get_property_key(title,'London','England', 'United Kingdom') == '208379f3bac1b0ac8548e12cf1097bbe'

def test_addition18():
    ft = CNFormatter()
    title = ft.title_formatter("The 1̲0̲0̲ S̲u̲n̲s̲e̲t̲ H̲o̲t̲e̲l̲ - ĊHŠẸ Ċệrtífíệd",'London','England', 'United Kingdom')
    assert  title == '100sunset'
    assert ft.get_property_key(title,'London','England', 'United Kingdom') == '208379f3bac1b0ac8548e12cf1097bbe'

def test_addition19():
    ft = CNFormatter()
    title = ft.title_formatter("The 100 Sűņşệţ Hôţệl - ĊHŜẸ Ċệrtífíệd",'London','England', 'United Kingdom')
    assert  title == '100sunset'
    assert ft.get_property_key(title,'London','England', 'United Kingdom') == '208379f3bac1b0ac8548e12cf1097bbe'

def test_addition20():
    ft = CNFormatter()
    title = ft.title_formatter("The 100 S̈ün̈s̈è̈ẗ Ḧöẗë̈l̈ - ĊĦŞẸ Ċệrtífíęd",'London','England', 'United Kingdom')
    assert  title == '100sunset'
    assert ft.get_property_key(title,'London','England', 'United Kingdom') == '208379f3bac1b0ac8548e12cf1097bbe'


def test_get_property_key():
    ft = CNFormatter()
    assert ft.get_property_key("The Queen's Gate Hotel",'London','England', 'United Kingdom') == '428c2485dd7e14535b88ab1a47556422'


    