
String media_path = "../../media/";
String out_path = "../../out/";

void setup() {
  PImage lena = loadImage(media_path + "lena.jpg");
  int lena_width=lena.width;
  int lena_height=lena.height;
  
  PImage plaza = loadImage(media_path + "plaza.png");
  plaza.resize(lena_width, lena_height);

  size(512, 512);
  
  image(plaza, 0, 0);
  
  lena.loadPixels();
  for (int i=0; i< lena.pixels.length; i++) {
      color c = lena.pixels[i];
      lena.pixels[i] = color(red(c),green(c),blue(c),127);
  }
  lena.updatePixels();

  image(lena, 0, 0);
  saveFrame(out_path + "lena-plaza.jpg");
}
