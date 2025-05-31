; ModuleID = 'autocfg_9839c7f03eec3e3b_9.589a19e85d562763-cgu.0'
source_filename = "autocfg_9839c7f03eec3e3b_9.589a19e85d562763-cgu.0"
target datalayout = "e-m:x-p:32:32-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32-a:0:32-S32"
target triple = "i686-pc-windows-msvc"

; core::f64::<impl f64>::to_ne_bytes
; Function Attrs: inlinehint uwtable
define internal void @"_ZN4core3f6421_$LT$impl$u20$f64$GT$11to_ne_bytes17hdf14edb0839eace2E"(ptr sret([8 x i8]) align 1 %_0, double %self) unnamed_addr #0 {
start:
  store double %self, ptr %_0, align 1
  ret void
}

; autocfg_9839c7f03eec3e3b_9::probe
; Function Attrs: uwtable
define void @_ZN26autocfg_9839c7f03eec3e3b_95probe17h3cef53280703fcc4E() unnamed_addr #1 {
start:
  %_1 = alloca [8 x i8], align 1
; call core::f64::<impl f64>::to_ne_bytes
  call void @"_ZN4core3f6421_$LT$impl$u20$f64$GT$11to_ne_bytes17hdf14edb0839eace2E"(ptr sret([8 x i8]) align 1 %_1, double 3.140000e+00)
  ret void
}

attributes #0 = { inlinehint uwtable "target-cpu"="pentium4" }
attributes #1 = { uwtable "target-cpu"="pentium4" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 8, !"PIC Level", i32 2}
!1 = !{!"rustc version 1.87.0 (17067e9ac 2025-05-09)"}
