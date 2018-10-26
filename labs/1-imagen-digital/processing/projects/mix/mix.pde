String media_path = "../../media/";
String out_path = "../../out/";
float rate = 0.5;

void setup(){
  PImage img_1 = loadImage(media_path + "plaza.png");
  PImage img_2 = loadImage(media_path + "lena.jpg");
  size(378, 568);
  img_1.loadPixels();
  img_2.loadPixels();
  for (int y=0; y<img_1.height; y++) {
    for (int x=0; x<img_1.width; x++) {
      color c_1 = img_1.get(x, y);
      color c_2 = img_2.get(x, y);
    
      img_1.set(x, y, color(
        red(c_1)*rate+red(c_2)*(1-rate),
        green(c_1)*rate+green(c_2)*(1-rate),
        blue(c_1)*rate+blue(c_2)*(1-rate)));
    }
    
    print(rate);
    print("\n");
  }
  image(img_1, 0, 0);
}
  