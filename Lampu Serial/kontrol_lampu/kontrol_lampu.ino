int x;
char a[30];     //Serial Read character buffer
byte b;         //Serial Read character to bytes buffer
byte iter,str_len;
String ac="", acc;   //Variable for complete instruction
void setup() {
  Serial.begin(57600);
  for (int i=0; i<=30; i++){
    a[i]=' ';
  }
  for (int i=2; i<=13; i++){
    pinMode(i, OUTPUT);
    digitalWrite(i, HIGH);
  }
  pinMode(A0, OUTPUT);
  digitalWrite(A0, HIGH);
}

void loop() {
  while (!Serial.available()){
  }
  while (Serial.available()){
    a[iter]=Serial.read();
    iter+=1;
    if (a[iter-1]==']')build_string();
    if (iter>=25)iter=0;      
  }

}

void build_string(){
  for (int i=0; i<=iter; i++){
    ac=ac+a[i];
  }
  //format ==[0,0,0,0,0,0,0,0,0,0,0,0];
  ac.trim();
  Serial.println(ac);
  byte len=ac.length();
  if (ac.startsWith("[") and ac.endsWith("]")){
    byte len=ac.length();
    byte pin=2;
    for (int i=1; i<=len;i+=2){
      if(i<=22){
        if(ac.substring(i,i+1)=="0")digitalWrite(pin,HIGH);
        if(ac.substring(i,i+1)=="1")digitalWrite(pin,LOW);
      }
      if(i>=23){
        if(ac.substring(i,i+1)=="0")digitalWrite(A0,HIGH);
        if(ac.substring(i,i+1)=="1")digitalWrite(A0,LOW);
      }
      pin+=1;
    }
    /*if (ac.substring(1,2)=="0")digitalWrite(2, HIGH); //stop relay1
    if (ac.substring(1,2)=="1")digitalWrite(2, LOW);  //start relay1
    if (ac.substring(3,4)=="0")digitalWrite(3, HIGH); //stop relay2
    if (ac.substring(3,4)=="1")digitalWrite(3, LOW);  //start relay2*/
  }
  for (int i=0; i<=30; i++){
    a[i]=' ';
  }
  ac="";
  iter=0;
}
