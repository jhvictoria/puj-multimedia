PImage imgLena;
PImage plaza;


void setup() {
  
  size(378, 568);
  imgLena = loadImage("lena.jpg");
  plaza = loadImage("plaza.png");
  
}

void draw() { 
  image(plaza,0,0);
  tint(255, 126);
  image(imgLena, 0, 0);  // Display at full opacity
  tint(255, 126);  // Display at half opacity
  save("mix.jpg");

}
