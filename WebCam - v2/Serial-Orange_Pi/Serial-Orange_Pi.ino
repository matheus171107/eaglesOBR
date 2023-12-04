#include <TFT_eSPI.h>
#include <SPI.h>


TFT_eSPI tft = TFT_eSPI(); 
String  msg;
char res, resant;
int vM1, vM2, c;
bool con = false;

void setup() {
  tft.init();
  Serial.begin(9600);
  tft.setRotation(1);
  tft.fillScreen(TFT_BLACK);

}

void loop() {
  if(Serial.available() != 0){
    res = Serial.read();
  }
  
  tft.setTextColor(TFT_WHITE);
  tft.setTextSize(2);
  tft.setCursor(10, 20);
  tft.println("Motor Esq.");
  tft.setTextColor(TFT_WHITE);
  tft.setCursor(190, 20);
  tft.println("Motor Dir.");
  tft.drawFastVLine(160, 0, 190, TFT_WHITE);
  tft.drawFastHLine(0, 190, 340, TFT_WHITE);

  if(res != resant){

    if(res == '1'){  //1 para Branco e 0 para Preto
      rest_tft();
      dirSeta('F', 'F');
      vM1 = 255; vM2 = 255;
      tft.setCursor(100, 210);
      tft.println("Linha Preta");

    }else if(res == '2'){
      rest_tft();
      //parada();
      dirSeta('F', 'F');   
      vM1 = 255; vM2 = 255;
      tft.setCursor(100, 210);
      tft.println("Cruzamento");

    }else if(res == '3'){
      rest_tft();
      //parada();
      dirSeta('T', 'F');
      vM1 = 255; vM2 = 255;
      tft.setCursor(100, 210);
      tft.println("Cruva 90 Esquerda");

    }else if(res == '4'){
      rest_tft();
      //parada();
      dirSeta('F', 'T');
      vM1 = 255; vM2 = 255;
      tft.setCursor(100, 210);
      tft.println("Curva 90 Direita");

    }else if(res == '5'){
      rest_tft();
      dirSeta('F','F');
      vM1 = 200; vM2 = 255;
      tft.setCursor(100, 210);
      tft.println("Alinhamento Esq.");

    }else if(res == '6'){
      rest_tft();
      dirSeta('F','F');
      vM1 = 255; vM2 = 200;
      tft.setCursor(100, 210);
      tft.println("Alinhamento Dir.");

    }else if(res == '7'){
      rest_tft();
      vM1 = 0; vM2 = 0;
      tft.setCursor(100, 210);
      tft.println("Rota Perdida");
    }else {
      rest_tft();
    }
}

  tft.setTextColor(TFT_RED);
  tft.setCursor(15, 90);
  tft.println("Vel: " + String(vM1));
  tft.setTextColor(TFT_RED);
  tft.setCursor(200, 90);
  tft.println("Vel: " + String(vM2));

  resant = res;

}

void dirSeta(char c1, char c2){
  if (c1 == 'F' && c2 == 'F'){
    tft.fillTriangle(130, 115, 115, 140, 145, 140, TFT_RED);
    tft.fillRect(120, 140, 20, 30, TFT_RED);

    tft.fillTriangle(190, 115, 175, 140, 205, 140, TFT_RED);
    tft.fillRect(180, 140, 20, 30, TFT_RED);
  }else if(c1 == 'T' && c2 == 'T'){
    tft.fillTriangle(130, 170, 115, 145, 145, 145, TFT_RED);
    tft.fillRect(120, 115, 20, 30, TFT_RED);

    tft.fillTriangle(190, 170, 175, 145, 205, 145, TFT_RED);
    tft.fillRect(180, 115, 20, 30, TFT_RED);
  }else if(c1 == 'F' && c2 == 'T'){
    tft.fillTriangle(130, 115, 115, 140, 145, 140, TFT_RED);
    tft.fillRect(120, 140, 20, 30, TFT_RED);

    tft.fillTriangle(190, 170, 175, 145, 205, 145, TFT_RED);
    tft.fillRect(180, 115, 20, 30, TFT_RED);
  }else if(c1 == 'T' && c2 == 'F'){
    tft.fillTriangle(130, 170, 115, 145, 145, 145, TFT_RED);
    tft.fillRect(120, 115, 20, 30, TFT_RED);

    tft.fillTriangle(190, 115, 175, 140, 205, 140, TFT_RED);
    tft.fillRect(180, 140, 20, 30, TFT_RED);
  }
}

void parada(){
  for (int c=3; c > 0; c--){
    tft.setCursor(100-(c*25), 210);
    tft.println(c);
    delay(1000);
  }
}

void rest_tft(){
  //tft.fillScreen(TFT_BLACK);
  tft.fillRect(0, 192, 340, 48, TFT_BLACK);
  tft.fillRect(60, 90, 60, 15, TFT_BLACK);
  tft.fillRect(245, 90, 60, 15, TFT_BLACK);
  tft.fillRect(115, 115, 35, 60, TFT_BLACK);
  tft.fillRect(175, 115, 35, 60, TFT_BLACK);

}

