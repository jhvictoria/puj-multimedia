PImage imgLena;
PImage plaza;


void setup() {
  
  color rgb;
  imgLena = loadImage("lena.jpg");
  plaza = loadImage("plaza.png");
  size(378, 568); //<>//
  image(plaza,0,0);
  imgLena.loadPixels();
  for(int i = 0 ; i<imgLena.pixels.length; i++){
       float r = red(imgLena.pixels[i]);
       float g = green(imgLena.pixels[i]);
       float b = blue(imgLena.pixels[i]);
       imgLena.pixels[i] = color(r,g,b,126);
  }
  image(imgLena,0,0);
  updatePixels();
  save("mix.jpg");

}
