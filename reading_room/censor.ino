#include <SoftwareSerial.h>
SoftwareSerial mySerial(2,3);
int sn=0;
int a=0,b=0,c=0,d=0;
char num;
int an,an2;
unsigned long tp, tc;
void setup(){
  mySerial.begin(9600);
  Serial.begin(9600);
  pinMode(6,INPUT);
  pinMode(7,INPUT);
  pinMode(4,INPUT);
  pinMode(5,INPUT);
  tp = millis();
  mySerial.println("AT+CIPSTART=\"TCP\",\"58.122.59.104\",80");
}
void loop(){
  if(digitalRead(6)==1&&a==0){
    sn=sn+1;
    a=1;
  }
  if(digitalRead(7)==1&&b==0){
    sn=sn+1;
    b=1;
  }
  if(digitalRead(4)==1&&c==0){
    sn=sn+1;
    c=1;
  }
  if(digitalRead(5)==1&&d==0){
    sn=sn+1;
    d=1;
  }
  if(Serial.available()){
    num=Serial.read();
    if(num=='a'){
      an=0;
      an2=0;
    }
    if(num=='0'){
      an=0;
    }
    else if(num=='1'){
      an=1;
    }
    else if(num=='2'){
      an=2;
    }
    else if(num=='3'){
      an=3;
    }
    else if(num=='4'){
      an=4;
    }
    else if(num=='5'){
      an=5;
    }
    else if(num=='6'){
      an=6;
    }
    else if(num=='7'){
      an=7;
    }
    else if(num=='8'){
      an=8;
    }
    else if(num=='9'){
      an=9;
    }
    an2*=10;
    an2+=an;
  }
  tc=millis();
  if(tc-tp>=1000){
    tp=tc;
    delay(200);
    String sendnum = "GET /iot/?title=%EC%84%A0%EB%A6%B0%EC%9D%B8%ED%84%B0%EB%84%B7%EA%B3%A0%EB%93%B1%ED%95%99%EA%B5%90%20%EB%8F%85%EC%84%9C%EC%8B%A4&len_person="+String(sn)+"&max_person="+String(an2)+"&x=37.542690&y=126.9677556 HTTP/1.1";
    int lengg = sendnum.length() + 4;
    String cipsend = "AT+CIPSEND="+String(lengg);
    mySerial.println(cipsend);
    delay(200);
    mySerial.println(sendnum);
    mySerial.println();
    sn=0;
    a=0;
    b=0;
    c=0;
    d=0;
  }
}