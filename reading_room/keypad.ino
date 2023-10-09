#include <LiquidCrystal_I2C.h>
#include <Keypad.h>
int a;
const byte ROWS = 4;
const byte COLS = 4;
char hexaKeys[ROWS][COLS] = {
  {'0', '1','2', '3'},
  {'4', '5', '6', '7'},
  {'8', '9','a', 'a'},
  {'a','a','a','a'}
};
byte rowPins[ROWS] = {9, 8, 7, 6};
byte colPins[COLS] = {10, 11, 12, 13};
char customKey;
char re;
Keypad customKeypad = Keypad( makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS);
LiquidCrystal_I2C lcd(0x27,16,2);
 
void setup() {
  Serial.begin(9600);
  lcd.begin();
  lcd.backlight();
  lcd.setCursor(0,0);
}
void keyPress();
 
void loop() {
  keyPress();
}
 
void keyPress() {                                 
  customKey = customKeypad.getKey();
  if (customKey) {
    Serial.print(customKey);
    if(customKey=='a'){
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("reset.");
      re = 'a';
    }
    else{
      if(re=='a'){
        lcd.clear();
        re ='0';
      }
      lcd.print(customKey);
    }
    delay(100);
  }
}