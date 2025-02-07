from IPython.display import HTML


def noticeWidget() -> HTML:
    content: str = """
      <div class="callout callout-style-default callout-caution callout-titled">
        <div class="callout-header d-flex align-content-center">
          <div class="callout-icon-container">
            <i class="callout-icon"></i>
          </div>
          <div class="callout-title-container flex-fill">
            Notice
          </div>
        </div>
        <div class="callout-body-container callout-body">
          <p>This blog is a work in progress. Follow me on <a href="https://www.linkedin.com/in/df-danielfilho/" target="_blank" data-original-href="https://www.linkedin.com/in/df-danielfilho/">LinkedIn</a> for updates.</p>
        </div>
      </div>
    """

    return HTML(content)
