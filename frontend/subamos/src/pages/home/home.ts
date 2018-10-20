import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { LoginPage } from '../login/login';
import { CategoriasPage } from '../categorias/categorias';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {

  constructor(public navCtrl: NavController) {

  }
  cerrarSesion(){
    localStorage.clear();
    this.navCtrl.setRoot(LoginPage);
  }

  mostrarcategorias(){
    this.navCtrl.push(CategoriasPage);
  }



}
