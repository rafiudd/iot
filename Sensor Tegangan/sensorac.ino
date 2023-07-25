const int jumlahMeja = 2;
const int mejaPins[jumlahMeja] = {2, 3};
int mejaSV[jumlahMeja];
int mejaStatus[jumlahMeja];

void setup() {
  Serial.begin(9600); // Memulai koneksi Serial Monitor

  for (int i = 0; i < jumlahMeja; i++) {
    pinMode(mejaPins[i], INPUT);
  }
}

void loop() {
  // Membaca nilai dari sensor tegangan pada setiap meja
  for (int i = 0; i < jumlahMeja; i++) {
    mejaSV[i] = digitalRead(mejaPins[i]);
  }

  for (int i = 0; i<jumlahMeja; i++){
    if (mejaSV[i] == 0){
      mejaStatus[i] = i + 1;
    }else{
      mejaStatus[i] = 0;
    }
  }

  printLampuStatus();

  // Menampilkan nilai output sensor dalam bentuk array pada Serial Monitor
  // Serial.print("[");
  // for (int i = 0; i < jumlahMeja; i++) {
  //   Serial.print(mejaSV[i]);
  //   if (i < jumlahMeja - 1) {
  //     Serial.print(", ");
  //   }
  // }
  // Serial.println("]");

  delay(2000);
}

void printLampuStatus() {
  Serial.print("[");
  bool isFirstLamp = true;

  for (int i = 0; i < jumlahMeja; i++) {
    if (mejaStatus[i]) {
      if (!isFirstLamp) {
        Serial.print(", ");
      }
      Serial.print(i + 1); // Menampilkan nomor lampu yang menyala (indeks + 1)
      isFirstLamp = false;
    }
  }
  Serial.println("]");
}
