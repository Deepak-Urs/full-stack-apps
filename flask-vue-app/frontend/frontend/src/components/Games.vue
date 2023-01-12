<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css"
        integrity="sha384-RxqHG2ilm4r6aFRpGmBbGTjsqwfqHOKy1ArsMhHusnRO47jcGqpIQqlQK/kmGy9R"
        crossorigin="anonymous"
      />
      <div class="row">
        <h1
          class="text-center bg-primary text-white"
          style="border-radius: 10px"
        >
          Games Library
        </h1>
        <hr />
        <br />
        <!-- alert message -->
        <b-alert variant="success" v-if="showMessage" show>
          {{ message }}
        </b-alert>

        <button
          type="button"
          class="btn btn-success btn-sm"
          v-b-modal.game-modal
        >
          Add Game
        </button>
        <br /><br />
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
            <tr v-for="(game, index) in games" :key="index">
              <td>{{ game.title }}</td>
              <td>{{ game.genre }}</td>
              <td>
                <span v-if="game.played">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                    type="button"
                    class="btn btn-info btn-sm"
                    v-b-modal.game-update-modal
                    @click="editGame(game)"
                  >
                    Update
                  </button>
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="deleteGame(game)"
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        <footer
          class="bg-primary text-white text-center"
          style="border-radius: 10px"
        >
          Copyright
        </footer>
      </div>

      <!-- first modal -->
      <b-modal
        ref="addGameModal"
        id="game-modal"
        title="Add a new game"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group
            id="form-title-group"
            label="Title:"
            label-for="form-title-input"
          >
            <b-form-input
              id="form-title-input"
              type="text"
              required
              v-model="addGameForm.title"
              placeholder="Enter Game"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group
            id="form-genre-group"
            label="genre:"
            label-for="form-genre-input"
          >
            <b-form-input
              id="form-genre-input"
              type="text"
              required
              v-model="addGameForm.genre"
              placeholder="Enter Game"
            >
            </b-form-input>
          </b-form-group>

          <!-- checkbox -->
          <b-form-group id="form-played-group">
            <b-form-checkbox-group
              v-model="addGameForm.played"
              id="form-checks"
            >
              <b-form-checkbox value="true"> Played? </b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>

          <!-- buttons: submit and reset -->
          <b-button type="submit" variant="outline-info">Submit</b-button>
          <b-button type="reset" variant="outline-danger">Reset</b-button>
        </b-form>
      </b-modal>
      <!--  end of modal-1 -->

      <!-- second modal -->
      <b-modal
        ref="editGameModal"
        id="game-modal"
        title="Update"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
          <b-form-group
            id="form-title-group"
            label="Title:"
            label-for="form-title-input"
          >
            <b-form-input
              id="form-title-input"
              type="text"
              required
              v-model="editForm.title"
              placeholder="Enter Game"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group
            id="form-genre-group"
            label="genre:"
            label-for="form-genre-input"
          >
            <b-form-input
              id="form-genre-input"
              type="text"
              required
              v-model="editForm.genre"
              placeholder="Enter Game"
            >
            </b-form-input>
          </b-form-group>

          <!-- checkbox -->
          <b-form-group id="form-played-group">
            <b-form-checkbox-group v-model="editForm.played" id="form-checks">
              <b-form-checkbox value="true"> Played? </b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>

          <!-- buttons: submit and reset -->
          <b-button type="submit" variant="outline-info">Update</b-button>
          <b-button type="reset" variant="outline-danger">Cancel</b-button>
        </b-form>
      </b-modal>
      <!-- end of second modal -->
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Shark-Component",
  data() {
    return {
      games: [],
      addGameForm: {
        title: "",
        genre: "",
        played: [],
      },
      editForm: {
        title: "",
        genre: "",
        played: [],
      },
    };
  },

  message: "",

  methods: {
    // Get function
    getGames() {
      const path = "http://localhost:5000/games";
      axios
        .get(path)
        .then((res) => {
          this.games = res.data.games;
        })
        .catch((err) => {
          console.log(err);
        });
    },

    addGame(payload) {
      const path = "http://localhost:5000/games";
      axios
        .post(path, payload)
        .then(() => {
          this.getGames();
          this.message = "Game Added!";
          this.showMessage = true;
        })
        .catch((err) => {
          console.log(err);
          this.getGames();
        });
    },

    // handle cancel btn click
    onResetUpdate(e) {
      e.preventDefault();
      this.$refs.editGameModal.hide();
      this.initForm();
      this.getGames();
    },

    onSubmitUpdate(e) {
      e.preventDefault();
      this.$refs.editGameModal.hide();
      let played = false;
      if (this.editForm.played[0]) {
        played = true;
      }
      const payload = {
        title: this.editGameForm.title,
        genre: this.editGameForm.genre,
        played,
      };
      this.updateGame(payload, this.editForm.id);
    },

    updateGame(payload, gameID) {
      const path = `http://localhost:5000/games/${gameID}`;
      axios
        .get(path, payload)
        .then(() => {
          this.getGames();
          this.message = "Game Updated!";
          this.showMessage = true;
        })
        .catch((err) => {
          console.log(err);
          this.getGames();
        });
    },

    // delete Individual game
    removeGame(gameID) {
      const path = `http://localhost:5000/games/${gameID}`;
      axios
        .delete(path)
        .then(() => {
          this.getGames();
          this.message = "Game Removed!";
          this.showMessage = true;
        })
        .catch((err) => {
          console.log(err);
          this.getGames();
        });
    },

    // handle Update btn
    editGame(game) {
      this.editForm = game;
    },

    // handle Delete btn
    deleteGame(game) {
      this.removeGame(game.id);
    },

    initForm() {
      this.addGameForm.title = "";
      this.addGameForm.genre = "";
      this.addGameForm.played = "";
      this.editForm.id = "";
      this.editForm.title = "";
      this.editForm.genre = "";
      this.editForm.played = [];
    },

    onSubmit(e) {
      e.preventDefault();
      let played = false;

      if (this.addGameForm[0]) {
        played = true;
      }
      const payload = {
        title: this.addGameForm.title,
        genre: this.addGameForm.genre,
        played,
      };

      this.addGame(payload);
      this.initForm();
      this.$refss.addGameModal.hide();
    },
    onReset(e) {
      e.preventDefault();
      this.$refs.addGameModal.hide();
      this.initForm();
    },
  },

  created() {
    this.getGames();
  },
};
</script>
