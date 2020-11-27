import getCookie from "./cookie.js";

const App = {
  data() {
    return {};
  },
  methods: {
    getUserAgreementOnDeleteProject(id) {
      const questionToUserAboutDeleteProject = confirm('Are you want to delete project ?');
      questionToUserAboutDeleteProject ? this.deleteProjectThroughApi(id) : console.log('Project not deleted');
    },
    deleteProjectThroughApi(id) {
      axios
        .delete(`http://127.0.0.1:8000/project-delete/${id}/`, {
          headers: {'X-CSRFToken': getCookie('csrftoken')}
        })
        .then(this.reloadPage())
        .catch(error => console.log(error));
    },
    reloadPage() {
      setTimeout(() => location.reload(), 500);
    }
  },
};

Vue.createApp(App).mount('#events');


