openerp.hr_loan = function (openerp) {
  "use strict";

  openerp.web_kanban.KanbanRecord.include({
      on_card_clicked: function() {
          if (this.view.dataset.model === 'hr.loan') {
              this.$('.oe_loans a').first().click();
          } else {
              this._super.apply(this, arguments);
          }
      },
  });

};
