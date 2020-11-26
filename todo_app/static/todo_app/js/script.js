const App = {
  data() {
    return {};
  },
  methods: {
    getUserAgreementOnDeleteProject(id) {
      const questionToUserAboutDeleteProject = confirm('Are you want to delete project ?');
      questionToUserAboutDeleteProject ? this.deleteProjectThroughApi(id) && location.reload() : console.log('Project not deleted');
    },
    deleteProjectThroughApi(id) {
      axios
        .delete(`http://127.0.0.1:8000/project-delete/${id}/`, {
          headers: {'X-CSRFToken': '0hekCQGnD4qwDkXxrQdMRCNQRyyoPW0fhxoGuttRaf1BQEbZBNEWQzPhjWEMKVLe'}
        })
        .then(response => (this.resultAboutDelete = response))
        .catch(error => console.log(error));
    },
  },
};

Vue.createApp(App).mount('#events');
