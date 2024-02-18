from viggocore.common import subsystem
from viggopayfac.subsystem.controle.pay_fac \
  import resource, router, manager
from viggopayfac.subsystem.controle.pay_fac import controller


subsystem = subsystem.Subsystem(resource=resource.PayFac,
                                manager=manager.Manager,
                                router=router.Router,
                                controller=controller.Controller)
