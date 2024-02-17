locals {
  jupyter-notebook-config-py-template = templatefile("${path.module}/files/jupyter/jupyter_server_config.py.tpl", {
    terminal_cull_inactive_timeout      = var.idle-culler-settings.terminal_cull_inactive_timeout
    terminal_cull_interval              = var.idle-culler-settings.terminal_cull_interval
    kernel_cull_idle_timeout            = var.idle-culler-settings.kernel_cull_idle_timeout
    kernel_cull_interval                = var.idle-culler-settings.kernel_cull_interval
    kernel_cull_connected               = var.idle-culler-settings.kernel_cull_connected ? "True" : "False" # for Python compatible boolean values
    kernel_cull_busy                    = var.idle-culler-settings.kernel_cull_busy ? "True" : "False"      # for Python compatible boolean values
    server_shutdown_no_activity_timeout = var.idle-culler-settings.server_shutdown_no_activity_timeout
    }
  )
}

locals {
  jupyter-pioneer-config-py-template = templatefile("${path.module}/files/jupyter/jupyter_jupyterlab_pioneer_config.py.tpl", {
    log_format = var.jupyterlab-pioneer-log-format != null ? var.jupyterlab-pioneer-log-format : ""
    }
  )
}


resource "local_file" "jupyter_server_config_py" {
  content  = local.jupyter-notebook-config-py-template
  filename = "${path.module}/files/jupyter/jupyter_server_config.py"
}

resource "local_file" "jupyter_jupyterlab_pioneer_config_py" {
  content  = local.jupyter-pioneer-config-py-template
  filename = "${path.module}/files/jupyter/jupyter_jupyterlab_pioneer_config.py"
}


resource "kubernetes_config_map" "etc-ipython" {
  metadata {
    name      = "etc-ipython"
    namespace = var.namespace
  }

  data = {
    for filename in fileset("${path.module}/files/ipython", "*") :
    filename => file("${path.module}/files/ipython/${filename}")
  }
}


locals {
  etc-jupyter-config-data = merge(
    {
      "jupyter_server_config.py" = local_file.jupyter_server_config_py.content,
    },
    var.jupyterlab-pioneer-enabled ? {
      # quotes are must here, as terraform would otherwise think py is a property of
      # a defined resource jupyter_jupyterlab_pioneer_config
      "jupyter_jupyterlab_pioneer_config.py" = local_file.jupyter_jupyterlab_pioneer_config_py.content
    } : {}
  )
}

resource "kubernetes_config_map" "etc-jupyter" {
  depends_on = [
    local_file.jupyter_server_config_py,
    local_file.jupyter_jupyterlab_pioneer_config_py
  ]

  metadata {
    name      = "etc-jupyter"
    namespace = var.namespace
  }

  data = local.etc-jupyter-config-data
}


resource "kubernetes_config_map" "etc-skel" {
  metadata {
    name      = "etc-skel"
    namespace = var.namespace
  }

  data = {
    for filename in fileset("${path.module}/files/skel", "*") :
    filename => file("${path.module}/files/skel/${filename}")
  }
}


resource "kubernetes_config_map" "jupyterlab-settings" {
  metadata {
    name      = "jupyterlab-settings"
    namespace = var.namespace
  }

  data = {
    for filename in fileset("${path.module}/files/jupyterlab", "*") :
    filename => file("${path.module}/files/jupyterlab/${filename}")
  }
}

resource "kubernetes_config_map" "git_clone_update" {
  metadata {
    name      = "git-clone-update"
    namespace = var.namespace
  }

  data = {
    "git-clone-update.sh" = "${file("${path.module}/files/extras/git_clone_update.sh")}"
  }
}
