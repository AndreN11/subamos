import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { LoginPage } from '../login/login';
import { CategoriasPage } from '../categorias/categorias';
import { Geolocation } from '@ionic-native/geolocation';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {

  constructor(public navCtrl: NavController, public geolocation: Geolocation) {

  }
   
    ionViewDidLoad(){
      this.obtenerPosicion();
    }

  
  cerrarSesion(){
    localStorage.clear();
    this.navCtrl.setRoot(LoginPage);
  }

  mostrarcategorias(){
    this.navCtrl.push(CategoriasPage);
  }

  obtenerPosicion() {
    this.geolocation.getCurrentPosition().then((coordenadas) => {
    console.log(coordenadas);
    }).catch((error) => {
    console.log('Error getting location', error);
    });
    }
}
