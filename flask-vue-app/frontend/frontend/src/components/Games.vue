<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css"
        integrity="sha384-RxqHG2ilm4r6aFRpGmBbGTjsqwfqHOKy1ArsMhHusnRO47jcGqpIQqlQK/kmGy9R" crossorigin="anonymous" />
      <div class="row">
        <h1 class="text-center bg-primary text-white" style="border-radius:10px">Games Library</h1>
        <hr />
        <br />
        <!-- alert message -->
        <button type="button" class="btn btn-success btn-sm" v-b-modal.game-modal>Add Game</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Genre</th>
              <th scope="col">Played</th>
              <th scope="col">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="game, index in games" :key="index">
              <td>{{ game.title }}</td>
              <td>{{ game.genre }}</td>
              <td>
                <span v-if="game.played">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-info btn-sm">
                    Update
                  </button>
                  <button type="button" class="btn btn-danger btn-sm">
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        <footer class="bg-primary text-white text-center" style="border-radius: 10px;">Copyright</footer>
      </div>

      <!-- first modal -->
      <b-modal ref="addGameModal" id="game-modal" title="Add a new game" hide-backdrop hide-footer>
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group id="form-title-group" label="Title:" label-for="form-title-input">
            <b-form-input id="form-title-input" type="text" required v-model="addGameForm.title"
              placeholder="Enter Game"></b-form-input>
          </b-form-group>

          <b-form-group id="form-genre-group" label="genre:" label-for="form-genre-input">
            <b-form-input id="form-genre-input" type="text" required v-model="addGameForm.genre"
              placeholder="Enter Game"></b-form-input>
          </b-form-group>

          <!-- checkbox -->
          <b-form-group id="form-played-group">
            <b-form-checkbox-group v-model="addGameForm.played" id="form-checks">
              <b-form-checkbox value="true"> Played? </b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>

          <!-- buttons: submit and reset -->
          <b-button type="submit" variant="outline-info">Submit</b-button>
          <b-button type="reset" variant="outline-danger">Reset</b-button>
        </b-form>

      </b-modal>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "Shark-Component",
  data() {
    return {
      games: [],
      addGameForm: {
        title: "",
        genre: "",
        played: [],
      }
    };
  },

  methods: {
    // Get function
    getGames() {
      const path = 'http://localhost:5000/games';
      axios.get(path)
        .then((res) => {
          this.games = res.data.games;
        })
        .catch((err) => {
          console.log(err);
        })
    },

    addGame(payload) {
      const path = 'http://localhost:5000/games';
      axios.post(path, payload)
      .then(() => {
        this.getGames();
      })
      .catch((err) => {
        console.log(err);
        this.getGames()
      })
    },

    initForm() {
      this.addGameForm.title = "";
      this.addGameForm.genre = "";
      this.addGameForm.played = "";
    },

    onSubmit(e) {
      e.preventDefault();
      this.$refs.addGameModal.hide()
      let played = false;

      if(this.addGameForm[0]) played = true;
      const payload = {
        title: this.addGameForm.title,
        genre: this.addGameForm.genre,
        played
      };

      this.addGameForm(payload);
      this.initForm;
    }
  },

  created() {
    this.getGames()
  }

};
</script>
