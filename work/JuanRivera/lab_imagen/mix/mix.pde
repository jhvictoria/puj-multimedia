void setup() //<>//
{
  PImage lenaI = loadImage("lena.jpg");
  PImage plazaI = loadImage("plaza.png");
  float factor = 126;
  size(378,568);
  tint(255,factor);
  image(plazaI,0,0);
  tint(255,255-factor);
  image(lenaI,0,0);
}
