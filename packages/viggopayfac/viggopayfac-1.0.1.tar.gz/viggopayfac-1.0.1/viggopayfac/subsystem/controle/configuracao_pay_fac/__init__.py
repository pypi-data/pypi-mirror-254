from viggocore.common import subsystem
from viggopayfac.subsystem.controle.configuracao_pay_fac \
  import resource, manager, router

subsystem = subsystem.Subsystem(resource=resource.ConfiguracaoPayFac,
                                manager=manager.Manager,
                                router=router.Router)
